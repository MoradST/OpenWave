import fs from 'node:fs';
import {createHash} from 'node:crypto';
const {APP_ID,API_KEY,GITHUB_EVENT_PATH}=process.env;
if(!APP_ID||!API_KEY){console.log('Push is not configured; skipping.');process.exit(0)}
const event=JSON.parse(fs.readFileSync(GITHUB_EVENT_PATH,'utf8'));
const issue=event.issue;
if(event.action!=='opened'||!issue||issue.state!=='open'||event.repository?.full_name!=='MoradST/OpenWave')process.exit(0);
const table=fs.readFileSync('README.md','utf8').split(/^## Topics\s*$/m)[1]?.split(/^## /m)[0]||'';
const map=new Map([['member','member'],['brand','brand']]);
for(const line of table.split('\n')){const m=line.match(/^\|\s*(.*?)\s*\|\s*`Topic: ([a-z0-9-]+)`\s*\|/);if(m){map.set(m[1].replace(/^[^a-zA-Z]+/,'').toLowerCase(),m[2]);map.set(m[2],m[2]);}}
map.set('podcasts','podcasts');
const prefix=issue.title.match(/^\[([^\]]+)\]/)?.[1]?.trim().toLowerCase();
const category=map.get(prefix);
if(!category){console.log('Not a recognized public post/profile.');process.exit(0)}
const title=issue.title.replace(/^\[[^\]]+\]\s*/,'').replace(/[\r\n]/g,' ').slice(0,140);
const id=createHash('sha256').update('openwave-issue-'+issue.id).digest('hex');const uuid=id.slice(0,8)+'-'+id.slice(8,12)+'-4'+id.slice(13,16)+'-a'+id.slice(17,20)+'-'+id.slice(20,32);
const payload={app_id:APP_ID,target_channel:'push',headings:{en:category==='member'?'OpenWave · New member':category==='brand'?'OpenWave · New brand':'OpenWave · '+prefix},contents:{en:title},url:'https://github.com/MoradST/OpenWave/issues/'+Number(issue.number),filters:[{field:'tag',key:'ow_all',relation:'=',value:'1'},{operator:'OR'},{field:'tag',key:'ow_'+category,relation:'=',value:'1'}],idempotency_key:uuid};
const r=await fetch('https://api.onesignal.com/notifications',{method:'POST',headers:{Authorization:'Key '+API_KEY,'Content-Type':'application/json'},body:JSON.stringify(payload)});
if(!r.ok)throw Error('Push provider returned HTTP '+r.status);
const result=await r.json();if(result.errors?.length)throw Error('Push provider reported an error');console.log('Push request accepted; delivery is not guaranteed.');
