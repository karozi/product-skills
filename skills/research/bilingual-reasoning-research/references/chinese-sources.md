# Chinese sources checklist for bilingual-reasoning-research

Read during **Phase 1b (ZH sweep)**. Check every domain in this list for every run. Log
`HIT` or `NO-HIT` per domain. A NO-HIT on a top-tier outlet is itself a finding — record it
in the Source Coverage Map.

## Query suffix matrix

Combine the topic's canonical name and its ZH variants (from the topic card) with every
suffix below. AI / developer-tool topics get every suffix; other topic types cherry-pick
the relevant subset.

| Suffix | Rough gloss | Use for |
|---|---|---|
| `发布` | launch / released | any product, model, feature |
| `评测` | review / benchmark | models, tools, hardware |
| `实测` | hands-on test | models, tools |
| `价格` | pricing | any paid product |
| `对比` | comparison | positioning vs domestic and Western rivals |
| `教程` | tutorial | developer tools, APIs |
| `踩坑` | pitfalls / gotchas | developer-community sentiment |
| `中转` | relay / API resale | Western AI APIs accessed from mainland |
| `国内使用` | domestic usage | access, geo-blocking, workarounds |
| `蒸馏` | distillation | model IP, anti-distillation posture |
| `开源` | open source | licensing, weights, community forks |
| `安全` | safety / security | policy, red-team, incidents |
| `监管` | regulation | policy framing, MIIT, CAC, TC260 |
| `融资` | funding | company topics |

## Domain checklist (top-tier and mid-tier)

### Tech media

- 36kr.com — 36Kr, mainstream tech + business.
- jiqizhixin.com — Synced (机器之心), AI-focused, technical.
- qbitai.com — QbitAI (量子位), AI + developer coverage.
- geekpark.net — GeekPark.
- ithome.com — IT之家, consumer tech + product news.
- sspai.com — 少数派, apps and dev tools.
- pingwest.com — PingWest.
- ifanr.com — 爱范儿.

### Developer communities

- juejin.cn — 掘金, technical write-ups and evals.
- csdn.net — CSDN, technical blogs (variable quality, high volume).
- infoq.cn — InfoQ China.
- oschina.net — 开源中国 (OSChina).
- v2ex.com — V2EX, developer forum sentiment.
- zhihu.com — 知乎, long-form Q&A, useful for framing.
- xueqiu.com — 雪球, investor-side takes on tech.

### Cloud + platform developer hubs

- cloud.tencent.com/developer — Tencent Cloud developer community.
- developer.aliyun.com — Alibaba Cloud developer community.
- bytedance.com and volcengine.com — ByteDance / Volcano Engine coverage.
- huaweicloud.com — Huawei Cloud, especially for models under sanctions framing.

### AI-lab first-party channels (as sources, not press)

- deepseek.com, qwen.ai (Alibaba), moonshot.cn (Kimi), zhipuai.cn (GLM), minimaxi.com,
  01.ai, doubao.com (ByteDance), hunyuan.tencent.com — read for divergence themes and
  domestic-comparison quotes.

### Social

- weibo.com — public commentary, sentiment.
- xiaohongshu.com — 小红书, consumer-side takes on AI products.
- bilibili.com — video demos and eval walkthroughs (skim titles and descriptions).

## Access notes

- Great Firewall behaviour: baidu.com, so.com (360), and sogou.com surface different result
  sets than Google. Use whichever search entry point the run environment can reach; log
  which was used in the Query Log.
- Tencent Cloud and Alibaba Cloud developer pages sometimes 403 on repeated fetches. Retry
  once, then log NO-HIT with reason `blocked`.
- Zhihu answers are often the highest-signal source for developer-community sentiment on
  Western AI launches. Prefer answers with 100+ upvotes and dated timestamps.

## Dedupe discipline

Chinese coverage of Western launches is heavily press-release derived. When 5+ articles
share identical phrasing on a claim, count them as one atomic claim and cite the earliest.
Original commentary (Zhihu long answers, Juejin write-ups, developer-forum threads) counts
separately even when it echoes the same fact — it's the framing that matters for the
Divergence Register.
