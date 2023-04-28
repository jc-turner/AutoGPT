# Auto-GPT: An Autonomous GPT-4 Experiment
[![Unit Tests](https://img.shields.io/github/actions/workflow/status/Significant-Gravitas/Auto-GPT/ci.yml?label=unit%20tests)](https://github.com/Significant-Gravitas/Auto-GPT/actions/workflows/ci.yml)
[![Discord Follow](https://dcbadge.vercel.app/api/server/autogpt?style=flat)](https://discord.gg/autogpt)
[![GitHub Repo stars](https://img.shields.io/github/stars/Significant-Gravitas/auto-gpt?style=social)](https://github.com/Significant-Gravitas/Auto-GPT/stargazers)
[![Twitter Follow](https://img.shields.io/twitter/follow/siggravitas?style=social)](https://twitter.com/SigGravitas)

English [简体中文](./README_zh-CN.md)

## 💡 Get help - [Q&A](https://github.com/Significant-Gravitas/Auto-GPT/discussions/categories/q-a) or [Discord 💬](https://discord.gg/autogpt)

<hr/>

### 🔴 🔴 🔴  Urgent: USE `stable` not `master`  🔴 🔴 🔴

**Download the latest `stable` release from here: https://github.com/Significant-Gravitas/Auto-GPT/releases/latest.**
The `master` branch may often be in a **broken** state.

<hr/>


Auto-GPT is an experimental open-source application showcasing the capabilities of the GPT-4 language model. This program, driven by GPT-4, chains together LLM "thoughts", to autonomously achieve whatever goal you set. As one of the first examples of GPT-4 running fully autonomously, Auto-GPT pushes the boundaries of what is possible with AI.

<h2 align="center"> Demo April 16th 2023 </h2>

https://user-images.githubusercontent.com/70048414/232352935-55c6bf7c-3958-406e-8610-0913475a0b05.mp4

Demo made by <a href=https://twitter.com/BlakeWerlinger>Blake Werlinger</a>

<h2 align="center"> 💖 Help Fund Auto-GPT's Development 💖</h2>
<p align="center">
If you can spare a coffee, you can help to cover the costs of developing Auto-GPT and help to push the boundaries of fully autonomous AI!
Your support is greatly appreciated. Development of this free, open-source project is made possible by all the <a href="https://github.com/Significant-Gravitas/Auto-GPT/graphs/contributors">contributors</a> and <a href="https://github.com/sponsors/Torantulino">sponsors</a>. If you'd like to sponsor this project and have your avatar or company logo appear below <a href="https://github.com/sponsors/Torantulino">click here</a>.
</p>


<p align="center">
<div align="center" class="logo-container">
<a href="https://www.zilliz.com/">
<picture height="40px">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/22963551/234158272-7917382e-ff80-469e-8d8c-94f4477b8b5a.png">
  <img src="https://user-images.githubusercontent.com/22963551/234158222-30e2d7a7-f0a9-433d-a305-e3aa0b194444.png" height="40px" alt="Zilliz" />
</picture>
</a>

<a href="https://roost.ai">
<img src="https://user-images.githubusercontent.com/22963551/234180283-b58cb03c-c95a-4196-93c1-28b52a388e9d.png" height="40px" alt="Roost.AI" />
</a>
<a href="https://nuclei.ai/">
<picture height="40px">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/22963551/234153428-24a6f31d-c0c6-4c9b-b3f4-9110148f67b4.png">
  <img src="https://user-images.githubusercontent.com/22963551/234181283-691c5d71-ca94-4646-a1cf-6e818bd86faa.png" height="40px" alt="NucleiAI" />
</picture>
</a>

<a href="https://www.algohash.org/">
<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/22963551/234180375-1365891c-0ba6-4d49-94c3-847c85fe03b0.png" >
  <img src="https://user-images.githubusercontent.com/22963551/234180359-143e4a7a-4a71-4830-99c8-9b165cde995f.png" height="40px" alt="Algohash" />
</picture>
</a>

<a href="https://www.typingmind.com/?utm_source=autogpt">
<picture height="40px">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/22963551/233202971-61e77209-58a0-47d9-9f7e-dd081111437b.png">
  <img src="https://user-images.githubusercontent.com/22963551/234157731-f908b5db-8fe7-4036-89b6-7b2a21f87e3a.png" height="40px" alt="TypingMind" />
</picture>
</a>

<a href="https://github.com/weaviate/weaviate">
<picture height="40px">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/22963551/234181699-3d7f6ea8-5a7f-4e98-b812-37be1081be4b.png">
  <img src="https://user-images.githubusercontent.com/22963551/234181695-fc895159-b921-4895-9a13-65e6eff5b0e7.png" height="40px" alt="TypingMind" />
</picture>
</a>

</div>
</br>



<p align="center"><a href="https://github.com/robinicus"><img src="https://avatars.githubusercontent.com/robinicus?v=4" width="50px" alt="robinicus" /></a>&nbsp;&nbsp;<a href="https://github.com/0xmatchmaker"><img src="https://avatars.githubusercontent.com/0xmatchmaker?v=4" width="50px" alt="0xmatchmaker" /></a>&nbsp;&nbsp;<a href="https://github.com/jazgarewal"><img src="https://avatars.githubusercontent.com/jazgarewal?v=4" width="50px" alt="jazgarewal" /></a>&nbsp;&nbsp;<a href="https://github.com/MayurVirkar"><img src="https://avatars.githubusercontent.com/MayurVirkar?v=4" width="50px" alt="MayurVirkar" /></a>&nbsp;&nbsp;<a href="https://github.com/avy-ai"><img src="https://avatars.githubusercontent.com/avy-ai?v=4" width="50px" alt="avy-ai" /></a>&nbsp;&nbsp;<a href="https://github.com/TheStoneMX"><img src="https://avatars.githubusercontent.com/TheStoneMX?v=4" width="50px" alt="TheStoneMX" /></a>&nbsp;&nbsp;<a href="https://github.com/goldenrecursion"><img src="https://avatars.githubusercontent.com/goldenrecursion?v=4" width="50px" alt="goldenrecursion" /></a>&nbsp;&nbsp;<a href="https://github.com/MatthewAgs"><img src="https://avatars.githubusercontent.com/MatthewAgs?v=4" width="50px" alt="MatthewAgs" /></a>&nbsp;&nbsp;<a href="https://github.com/eelbaz"><img src="https://avatars.githubusercontent.com/eelbaz?v=4" width="50px" alt="eelbaz" /></a>&nbsp;&nbsp;<a href="https://github.com/rapidstartup"><img src="https://avatars.githubusercontent.com/rapidstartup?v=4" width="50px" alt="rapidstartup" /></a>&nbsp;&nbsp;<a href="https://github.com/gklab"><img src="https://avatars.githubusercontent.com/gklab?v=4" width="50px" alt="gklab" /></a>&nbsp;&nbsp;<a href="https://github.com/VoiceBeer"><img src="https://avatars.githubusercontent.com/VoiceBeer?v=4" width="50px" alt="VoiceBeer" /></a>&nbsp;&nbsp;<a href="https://github.com/DailyBotHQ"><img src="https://avatars.githubusercontent.com/DailyBotHQ?v=4" width="50px" alt="DailyBotHQ" /></a>&nbsp;&nbsp;<a href="https://github.com/lucas-chu"><img src="https://avatars.githubusercontent.com/lucas-chu?v=4" width="50px" alt="lucas-chu" /></a>&nbsp;&nbsp;<a href="https://github.com/knifour"><img src="https://avatars.githubusercontent.com/knifour?v=4" width="50px" alt="knifour" /></a>&nbsp;&nbsp;<a href="https://github.com/refinery1"><img src="https://avatars.githubusercontent.com/refinery1?v=4" width="50px" alt="refinery1" /></a>&nbsp;&nbsp;<a href="https://github.com/st617"><img src="https://avatars.githubusercontent.com/st617?v=4" width="50px" alt="st617" /></a>&nbsp;&nbsp;<a href="https://github.com/neodenit"><img src="https://avatars.githubusercontent.com/neodenit?v=4" width="50px" alt="neodenit" /></a>&nbsp;&nbsp;<a href="https://github.com/CrazySwami"><img src="https://avatars.githubusercontent.com/CrazySwami?v=4" width="50px" alt="CrazySwami" /></a>&nbsp;&nbsp;<a href="https://github.com/Heitechsoft"><img src="https://avatars.githubusercontent.com/Heitechsoft?v=4" width="50px" alt="Heitechsoft" /></a>&nbsp;&nbsp;<a href="https://github.com/RealChrisSean"><img src="https://avatars.githubusercontent.com/RealChrisSean?v=4" width="50px" alt="RealChrisSean" /></a>&nbsp;&nbsp;<a href="https://github.com/abhinav-pandey29"><img src="https://avatars.githubusercontent.com/abhinav-pandey29?v=4" width="50px" alt="abhinav-pandey29" /></a>&nbsp;&nbsp;<a href="https://github.com/Explorergt92"><img src="https://avatars.githubusercontent.com/Explorergt92?v=4" width="50px" alt="Explorergt92" /></a>&nbsp;&nbsp;<a href="https://github.com/SparkplanAI"><img src="https://avatars.githubusercontent.com/SparkplanAI?v=4" width="50px" alt="SparkplanAI" /></a>&nbsp;&nbsp;<a href="https://github.com/crizzler"><img src="https://avatars.githubusercontent.com/crizzler?v=4" width="50px" alt="crizzler" /></a>&nbsp;&nbsp;<a href="https://github.com/kreativai"><img src="https://avatars.githubusercontent.com/kreativai?v=4" width="50px" alt="kreativai" /></a>&nbsp;&nbsp;<a href="https://github.com/omphos"><img src="https://avatars.githubusercontent.com/omphos?v=4" width="50px" alt="omphos" /></a>&nbsp;&nbsp;<a href="https://github.com/Jahmazon"><img src="https://avatars.githubusercontent.com/Jahmazon?v=4" width="50px" alt="Jahmazon" /></a>&nbsp;&nbsp;<a href="https://github.com/tjarmain"><img src="https://avatars.githubusercontent.com/tjarmain?v=4" width="50px" alt="tjarmain" /></a>&nbsp;&nbsp;<a href="https://github.com/ddtarazona"><img src="https://avatars.githubusercontent.com/ddtarazona?v=4" width="50px" alt="ddtarazona" /></a>&nbsp;&nbsp;<a href="https://github.com/saten-private"><img src="https://avatars.githubusercontent.com/saten-private?v=4" width="50px" alt="saten-private" /></a>&nbsp;&nbsp;<a href="https://github.com/anvarazizov"><img src="https://avatars.githubusercontent.com/anvarazizov?v=4" width="50px" alt="anvarazizov" /></a>&nbsp;&nbsp;<a href="https://github.com/lazzacapital"><img src="https://avatars.githubusercontent.com/lazzacapital?v=4" width="50px" alt="lazzacapital" /></a>&nbsp;&nbsp;<a href="https://github.com/m"><img src="https://avatars.githubusercontent.com/m?v=4" width="50px" alt="m" /></a>&nbsp;&nbsp;<a href="https://github.com/Pythagora-io"><img src="https://avatars.githubusercontent.com/Pythagora-io?v=4" width="50px" alt="Pythagora-io" /></a>&nbsp;&nbsp;<a href="https://github.com/Web3Capital"><img src="https://avatars.githubusercontent.com/Web3Capital?v=4" width="50px" alt="Web3Capital" /></a>&nbsp;&nbsp;<a href="https://github.com/toverly1"><img src="https://avatars.githubusercontent.com/toverly1?v=4" width="50px" alt="toverly1" /></a>&nbsp;&nbsp;<a href="https://github.com/digisomni"><img src="https://avatars.githubusercontent.com/digisomni?v=4" width="50px" alt="digisomni" /></a>&nbsp;&nbsp;<a href="https://github.com/concreit"><img src="https://avatars.githubusercontent.com/concreit?v=4" width="50px" alt="concreit" /></a>&nbsp;&nbsp;<a href="https://github.com/LeeRobidas"><img src="https://avatars.githubusercontent.com/LeeRobidas?v=4" width="50px" alt="LeeRobidas" /></a>&nbsp;&nbsp;<a href="https://github.com/Josecodesalot"><img src="https://avatars.githubusercontent.com/Josecodesalot?v=4" width="50px" alt="Josecodesalot" /></a>&nbsp;&nbsp;<a href="https://github.com/dexterityx"><img src="https://avatars.githubusercontent.com/dexterityx?v=4" width="50px" alt="dexterityx" /></a>&nbsp;&nbsp;<a href="https://github.com/rickscode"><img src="https://avatars.githubusercontent.com/rickscode?v=4" width="50px" alt="rickscode" /></a>&nbsp;&nbsp;<a href="https://github.com/Brodie0"><img src="https://avatars.githubusercontent.com/Brodie0?v=4" width="50px" alt="Brodie0" /></a>&nbsp;&nbsp;<a href="https://github.com/FSTatSBS"><img src="https://avatars.githubusercontent.com/FSTatSBS?v=4" width="50px" alt="FSTatSBS" /></a>&nbsp;&nbsp;<a href="https://github.com/nocodeclarity"><img src="https://avatars.githubusercontent.com/nocodeclarity?v=4" width="50px" alt="nocodeclarity" /></a>&nbsp;&nbsp;<a href="https://github.com/jsolejr"><img src="https://avatars.githubusercontent.com/jsolejr?v=4" width="50px" alt="jsolejr" /></a>&nbsp;&nbsp;<a href="https://github.com/amr-elsehemy"><img src="https://avatars.githubusercontent.com/amr-elsehemy?v=4" width="50px" alt="amr-elsehemy" /></a>&nbsp;&nbsp;<a href="https://github.com/RawBanana"><img src="https://avatars.githubusercontent.com/RawBanana?v=4" width="50px" alt="RawBanana" /></a>&nbsp;&nbsp;<a href="https://github.com/horazius"><img src="https://avatars.githubusercontent.com/horazius?v=4" width="50px" alt="horazius" /></a>&nbsp;&nbsp;<a href="https://github.com/SwftCoins"><img src="https://avatars.githubusercontent.com/SwftCoins?v=4" width="50px" alt="SwftCoins" /></a>&nbsp;&nbsp;<a href="https://github.com/tob-le-rone"><img src="https://avatars.githubusercontent.com/tob-le-rone?v=4" width="50px" alt="tob-le-rone" /></a>&nbsp;&nbsp;<a href="https://github.com/RThaweewat"><img src="https://avatars.githubusercontent.com/RThaweewat?v=4" width="50px" alt="RThaweewat" /></a>&nbsp;&nbsp;<a href="https://github.com/jun784"><img src="https://avatars.githubusercontent.com/jun784?v=4" width="50px" alt="jun784" /></a>&nbsp;&nbsp;<a href="https://github.com/joaomdmoura"><img src="https://avatars.githubusercontent.com/joaomdmoura?v=4" width="50px" alt="joaomdmoura" /></a>&nbsp;&nbsp;<a href="https://github.com/rejunity"><img src="https://avatars.githubusercontent.com/rejunity?v=4" width="50px" alt="rejunity" /></a>&nbsp;&nbsp;<a href="https://github.com/mathewhawkins"><img src="https://avatars.githubusercontent.com/mathewhawkins?v=4" width="50px" alt="mathewhawkins" /></a>&nbsp;&nbsp;<a href="https://github.com/caitlynmeeks"><img src="https://avatars.githubusercontent.com/caitlynmeeks?v=4" width="50px" alt="caitlynmeeks" /></a>&nbsp;&nbsp;<a href="https://github.com/jd3655"><img src="https://avatars.githubusercontent.com/jd3655?v=4" width="50px" alt="jd3655" /></a>&nbsp;&nbsp;<a href="https://github.com/Odin519Tomas"><img src="https://avatars.githubusercontent.com/Odin519Tomas?v=4" width="50px" alt="Odin519Tomas" /></a>&nbsp;&nbsp;<a href="https://github.com/DataMetis"><img src="https://avatars.githubusercontent.com/DataMetis?v=4" width="50px" alt="DataMetis" /></a>&nbsp;&nbsp;<a href="https://github.com/webbcolton"><img src="https://avatars.githubusercontent.com/webbcolton?v=4" width="50px" alt="webbcolton" /></a>&nbsp;&nbsp;<a href="https://github.com/rocks6"><img src="https://avatars.githubusercontent.com/rocks6?v=4" width="50px" alt="rocks6" /></a>&nbsp;&nbsp;<a href="https://github.com/cxs"><img src="https://avatars.githubusercontent.com/cxs?v=4" width="50px" alt="cxs" /></a>&nbsp;&nbsp;<a href="https://github.com/fruition"><img src="https://avatars.githubusercontent.com/fruition?v=4" width="50px" alt="fruition" /></a>&nbsp;&nbsp;<a href="https://github.com/nnkostov"><img src="https://avatars.githubusercontent.com/nnkostov?v=4" width="50px" alt="nnkostov" /></a>&nbsp;&nbsp;<a href="https://github.com/morcos"><img src="https://avatars.githubusercontent.com/morcos?v=4" width="50px" alt="morcos" /></a>&nbsp;&nbsp;<a href="https://github.com/pingbotan"><img src="https://avatars.githubusercontent.com/pingbotan?v=4" width="50px" alt="pingbotan" /></a>&nbsp;&nbsp;<a href="https://github.com/maxxflyer"><img src="https://avatars.githubusercontent.com/maxxflyer?v=4" width="50px" alt="maxxflyer" /></a>&nbsp;&nbsp;<a href="https://github.com/tommi-joentakanen"><img src="https://avatars.githubusercontent.com/tommi-joentakanen?v=4" width="50px" alt="tommi-joentakanen" /></a>&nbsp;&nbsp;<a href="https://github.com/hunteraraujo"><img src="https://avatars.githubusercontent.com/hunteraraujo?v=4" width="50px" alt="hunteraraujo" /></a>&nbsp;&nbsp;<a href="https://github.com/projectonegames"><img src="https://avatars.githubusercontent.com/projectonegames?v=4" width="50px" alt="projectonegames" /></a>&nbsp;&nbsp;<a href="https://github.com/tullytim"><img src="https://avatars.githubusercontent.com/tullytim?v=4" width="50px" alt="tullytim" /></a>&nbsp;&nbsp;<a href="https://github.com/comet-ml"><img src="https://avatars.githubusercontent.com/comet-ml?v=4" width="50px" alt="comet-ml" /></a>&nbsp;&nbsp;<a href="https://github.com/thepok"><img src="https://avatars.githubusercontent.com/thepok?v=4" width="50px" alt="thepok" /></a>&nbsp;&nbsp;<a href="https://github.com/prompthero"><img src="https://avatars.githubusercontent.com/prompthero?v=4" width="50px" alt="prompthero" /></a>&nbsp;&nbsp;<a href="https://github.com/sunchongren"><img src="https://avatars.githubusercontent.com/sunchongren?v=4" width="50px" alt="sunchongren" /></a>&nbsp;&nbsp;<a href="https://github.com/neverinstall"><img src="https://avatars.githubusercontent.com/neverinstall?v=4" width="50px" alt="neverinstall" /></a>&nbsp;&nbsp;<a href="https://github.com/josephcmiller2"><img src="https://avatars.githubusercontent.com/josephcmiller2?v=4" width="50px" alt="josephcmiller2" /></a>&nbsp;&nbsp;<a href="https://github.com/yx3110"><img src="https://avatars.githubusercontent.com/yx3110?v=4" width="50px" alt="yx3110" /></a>&nbsp;&nbsp;<a href="https://github.com/MBassi91"><img src="https://avatars.githubusercontent.com/MBassi91?v=4" width="50px" alt="MBassi91" /></a>&nbsp;&nbsp;<a href="https://github.com/SpacingLily"><img src="https://avatars.githubusercontent.com/SpacingLily?v=4" width="50px" alt="SpacingLily" /></a>&nbsp;&nbsp;<a href="https://github.com/arthur-x88"><img src="https://avatars.githubusercontent.com/arthur-x88?v=4" width="50px" alt="arthur-x88" /></a>&nbsp;&nbsp;<a href="https://github.com/ciscodebs"><img src="https://avatars.githubusercontent.com/ciscodebs?v=4" width="50px" alt="ciscodebs" /></a>&nbsp;&nbsp;<a href="https://github.com/christian-gheorghe"><img src="https://avatars.githubusercontent.com/christian-gheorghe?v=4" width="50px" alt="christian-gheorghe" /></a>&nbsp;&nbsp;<a href="https://github.com/EngageStrategies"><img src="https://avatars.githubusercontent.com/EngageStrategies?v=4" width="50px" alt="EngageStrategies" /></a>&nbsp;&nbsp;<a href="https://github.com/jondwillis"><img src="https://avatars.githubusercontent.com/jondwillis?v=4" width="50px" alt="jondwillis" /></a>&nbsp;&nbsp;<a href="https://github.com/Cameron-Fulton"><img src="https://avatars.githubusercontent.com/Cameron-Fulton?v=4" width="50px" alt="Cameron-Fulton" /></a>&nbsp;&nbsp;<a href="https://github.com/AryaXAI"><img src="https://avatars.githubusercontent.com/AryaXAI?v=4" width="50px" alt="AryaXAI" /></a>&nbsp;&nbsp;<a href="https://github.com/AuroraHolding"><img src="https://avatars.githubusercontent.com/AuroraHolding?v=4" width="50px" alt="AuroraHolding" /></a>&nbsp;&nbsp;<a href="https://github.com/Mr-Bishop42"><img src="https://avatars.githubusercontent.com/Mr-Bishop42?v=4" width="50px" alt="Mr-Bishop42" /></a>&nbsp;&nbsp;<a href="https://github.com/doverhq"><img src="https://avatars.githubusercontent.com/doverhq?v=4" width="50px" alt="doverhq" /></a>&nbsp;&nbsp;<a href="https://github.com/johnculkin"><img src="https://avatars.githubusercontent.com/johnculkin?v=4" width="50px" alt="johnculkin" /></a>&nbsp;&nbsp;<a href="https://github.com/marv-technology"><img src="https://avatars.githubusercontent.com/marv-technology?v=4" width="50px" alt="marv-technology" /></a>&nbsp;&nbsp;<a href="https://github.com/ikarosai"><img src="https://avatars.githubusercontent.com/ikarosai?v=4" width="50px" alt="ikarosai" /></a>&nbsp;&nbsp;<a href="https://github.com/ColinConwell"><img src="https://avatars.githubusercontent.com/ColinConwell?v=4" width="50px" alt="ColinConwell" /></a>&nbsp;&nbsp;<a href="https://github.com/humungasaurus"><img src="https://avatars.githubusercontent.com/humungasaurus?v=4" width="50px" alt="humungasaurus" /></a>&nbsp;&nbsp;<a href="https://github.com/terpsfreak"><img src="https://avatars.githubusercontent.com/terpsfreak?v=4" width="50px" alt="terpsfreak" /></a>&nbsp;&nbsp;<a href="https://github.com/iddelacruz"><img src="https://avatars.githubusercontent.com/iddelacruz?v=4" width="50px" alt="iddelacruz" /></a>&nbsp;&nbsp;<a href="https://github.com/thisisjeffchen"><img src="https://avatars.githubusercontent.com/thisisjeffchen?v=4" width="50px" alt="thisisjeffchen" /></a>&nbsp;&nbsp;<a href="https://github.com/nicoguyon"><img src="https://avatars.githubusercontent.com/nicoguyon?v=4" width="50px" alt="nicoguyon" /></a>&nbsp;&nbsp;<a href="https://github.com/arjunb023"><img src="https://avatars.githubusercontent.com/arjunb023?v=4" width="50px" alt="arjunb023" /></a>&nbsp;&nbsp;<a href="https://github.com/Nalhos"><img src="https://avatars.githubusercontent.com/Nalhos?v=4" width="50px" alt="Nalhos" /></a>&nbsp;&nbsp;<a href="https://github.com/belharethsami"><img src="https://avatars.githubusercontent.com/belharethsami?v=4" width="50px" alt="belharethsami" /></a>&nbsp;&nbsp;<a href="https://github.com/Mobivs"><img src="https://avatars.githubusercontent.com/Mobivs?v=4" width="50px" alt="Mobivs" /></a>&nbsp;&nbsp;<a href="https://github.com/txtr99"><img src="https://avatars.githubusercontent.com/txtr99?v=4" width="50px" alt="txtr99" /></a>&nbsp;&nbsp;<a href="https://github.com/ntwrite"><img src="https://avatars.githubusercontent.com/ntwrite?v=4" width="50px" alt="ntwrite" /></a>&nbsp;&nbsp;<a href="https://github.com/founderblocks-sils"><img src="https://avatars.githubusercontent.com/founderblocks-sils?v=4" width="50px" alt="founderblocks-sils" /></a>&nbsp;&nbsp;<a href="https://github.com/kMag410"><img src="https://avatars.githubusercontent.com/kMag410?v=4" width="50px" alt="kMag410" /></a>&nbsp;&nbsp;<a href="https://github.com/angiaou"><img src="https://avatars.githubusercontent.com/angiaou?v=4" width="50px" alt="angiaou" /></a>&nbsp;&nbsp;<a href="https://github.com/garythebat"><img src="https://avatars.githubusercontent.com/garythebat?v=4" width="50px" alt="garythebat" /></a>&nbsp;&nbsp;<a href="https://github.com/lmaugustin"><img src="https://avatars.githubusercontent.com/lmaugustin?v=4" width="50px" alt="lmaugustin" /></a>&nbsp;&nbsp;<a href="https://github.com/shawnharmsen"><img src="https://avatars.githubusercontent.com/shawnharmsen?v=4" width="50px" alt="shawnharmsen" /></a>&nbsp;&nbsp;<a href="https://github.com/clortegah"><img src="https://avatars.githubusercontent.com/clortegah?v=4" width="50px" alt="clortegah" /></a>&nbsp;&nbsp;<a href="https://github.com/MetaPath01"><img src="https://avatars.githubusercontent.com/MetaPath01?v=4" width="50px" alt="MetaPath01" /></a>&nbsp;&nbsp;<a href="https://github.com/sekomike910"><img src="https://avatars.githubusercontent.com/sekomike910?v=4" width="50px" alt="sekomike910" /></a>&nbsp;&nbsp;<a href="https://github.com/MediConCenHK"><img src="https://avatars.githubusercontent.com/MediConCenHK?v=4" width="50px" alt="MediConCenHK" /></a>&nbsp;&nbsp;<a href="https://github.com/svpermari0"><img src="https://avatars.githubusercontent.com/svpermari0?v=4" width="50px" alt="svpermari0" /></a>&nbsp;&nbsp;<a href="https://github.com/jacobyoby"><img src="https://avatars.githubusercontent.com/jacobyoby?v=4" width="50px" alt="jacobyoby" /></a>&nbsp;&nbsp;<a href="https://github.com/turintech"><img src="https://avatars.githubusercontent.com/turintech?v=4" width="50px" alt="turintech" /></a>&nbsp;&nbsp;<a href="https://github.com/allenstecat"><img src="https://avatars.githubusercontent.com/allenstecat?v=4" width="50px" alt="allenstecat" /></a>&nbsp;&nbsp;<a href="https://github.com/CatsMeow492"><img src="https://avatars.githubusercontent.com/CatsMeow492?v=4" width="50px" alt="CatsMeow492" /></a>&nbsp;&nbsp;<a href="https://github.com/tommygeee"><img src="https://avatars.githubusercontent.com/tommygeee?v=4" width="50px" alt="tommygeee" /></a>&nbsp;&nbsp;<a href="https://github.com/judegomila"><img src="https://avatars.githubusercontent.com/judegomila?v=4" width="50px" alt="judegomila" /></a>&nbsp;&nbsp;<a href="https://github.com/cfarquhar"><img src="https://avatars.githubusercontent.com/cfarquhar?v=4" width="50px" alt="cfarquhar" /></a>&nbsp;&nbsp;<a href="https://github.com/ZoneSixGames"><img src="https://avatars.githubusercontent.com/ZoneSixGames?v=4" width="50px" alt="ZoneSixGames" /></a>&nbsp;&nbsp;<a href="https://github.com/kenndanielso"><img src="https://avatars.githubusercontent.com/kenndanielso?v=4" width="50px" alt="kenndanielso" /></a>&nbsp;&nbsp;<a href="https://github.com/CrypteorCapital"><img src="https://avatars.githubusercontent.com/CrypteorCapital?v=4" width="50px" alt="CrypteorCapital" /></a>&nbsp;&nbsp;<a href="https://github.com/sultanmeghji"><img src="https://avatars.githubusercontent.com/sultanmeghji?v=4" width="50px" alt="sultanmeghji" /></a>&nbsp;&nbsp;<a href="https://github.com/jenius-eagle"><img src="https://avatars.githubusercontent.com/jenius-eagle?v=4" width="50px" alt="jenius-eagle" /></a>&nbsp;&nbsp;<a href="https://github.com/josephjacks"><img src="https://avatars.githubusercontent.com/josephjacks?v=4" width="50px" alt="josephjacks" /></a>&nbsp;&nbsp;<a href="https://github.com/pingshian0131"><img src="https://avatars.githubusercontent.com/pingshian0131?v=4" width="50px" alt="pingshian0131" /></a>&nbsp;&nbsp;<a href="https://github.com/AIdevelopersAI"><img src="https://avatars.githubusercontent.com/AIdevelopersAI?v=4" width="50px" alt="AIdevelopersAI" /></a>&nbsp;&nbsp;<a href="https://github.com/ternary5"><img src="https://avatars.githubusercontent.com/ternary5?v=4" width="50px" alt="ternary5" /></a>&nbsp;&nbsp;<a href="https://github.com/ChrisDMT"><img src="https://avatars.githubusercontent.com/ChrisDMT?v=4" width="50px" alt="ChrisDMT" /></a>&nbsp;&nbsp;<a href="https://github.com/AcountoOU"><img src="https://avatars.githubusercontent.com/AcountoOU?v=4" width="50px" alt="AcountoOU" /></a>&nbsp;&nbsp;<a href="https://github.com/chatgpt-prompts"><img src="https://avatars.githubusercontent.com/chatgpt-prompts?v=4" width="50px" alt="chatgpt-prompts" /></a>&nbsp;&nbsp;<a href="https://github.com/Partender"><img src="https://avatars.githubusercontent.com/Partender?v=4" width="50px" alt="Partender" /></a>&nbsp;&nbsp;<a href="https://github.com/Daniel1357"><img src="https://avatars.githubusercontent.com/Daniel1357?v=4" width="50px" alt="Daniel1357" /></a>&nbsp;&nbsp;<a href="https://github.com/KiaArmani"><img src="https://avatars.githubusercontent.com/KiaArmani?v=4" width="50px" alt="KiaArmani" /></a>&nbsp;&nbsp;<a href="https://github.com/zkonduit"><img src="https://avatars.githubusercontent.com/zkonduit?v=4" width="50px" alt="zkonduit" /></a>&nbsp;&nbsp;<a href="https://github.com/fabrietech"><img src="https://avatars.githubusercontent.com/fabrietech?v=4" width="50px" alt="fabrietech" /></a>&nbsp;&nbsp;<a href="https://github.com/scryptedinc"><img src="https://avatars.githubusercontent.com/scryptedinc?v=4" width="50px" alt="scryptedinc" /></a>&nbsp;&nbsp;<a href="https://github.com/coreyspagnoli"><img src="https://avatars.githubusercontent.com/coreyspagnoli?v=4" width="50px" alt="coreyspagnoli" /></a>&nbsp;&nbsp;<a href="https://github.com/AntonioCiolino"><img src="https://avatars.githubusercontent.com/AntonioCiolino?v=4" width="50px" alt="AntonioCiolino" /></a>&nbsp;&nbsp;<a href="https://github.com/Dradstone"><img src="https://avatars.githubusercontent.com/Dradstone?v=4" width="50px" alt="Dradstone" /></a>&nbsp;&nbsp;<a href="https://github.com/CarmenCocoa"><img src="https://avatars.githubusercontent.com/CarmenCocoa?v=4" width="50px" alt="CarmenCocoa" /></a>&nbsp;&nbsp;<a href="https://github.com/bentoml"><img src="https://avatars.githubusercontent.com/bentoml?v=4" width="50px" alt="bentoml" /></a>&nbsp;&nbsp;<a href="https://github.com/merwanehamadi"><img src="https://avatars.githubusercontent.com/merwanehamadi?v=4" width="50px" alt="merwanehamadi" /></a>&nbsp;&nbsp;<a href="https://github.com/vkozacek"><img src="https://avatars.githubusercontent.com/vkozacek?v=4" width="50px" alt="vkozacek" /></a>&nbsp;&nbsp;<a href="https://github.com/ASmithOWL"><img src="https://avatars.githubusercontent.com/ASmithOWL?v=4" width="50px" alt="ASmithOWL" /></a>&nbsp;&nbsp;<a href="https://github.com/tekelsey"><img src="https://avatars.githubusercontent.com/tekelsey?v=4" width="50px" alt="tekelsey" /></a>&nbsp;&nbsp;<a href="https://github.com/GalaxyVideoAgency"><img src="https://avatars.githubusercontent.com/GalaxyVideoAgency?v=4" width="50px" alt="GalaxyVideoAgency" /></a>&nbsp;&nbsp;<a href="https://github.com/wenfengwang"><img src="https://avatars.githubusercontent.com/wenfengwang?v=4" width="50px" alt="wenfengwang" /></a>&nbsp;&nbsp;<a href="https://github.com/rviramontes"><img src="https://avatars.githubusercontent.com/rviramontes?v=4" width="50px" alt="rviramontes" /></a>&nbsp;&nbsp;<a href="https://github.com/indoor47"><img src="https://avatars.githubusercontent.com/indoor47?v=4" width="50px" alt="indoor47" /></a>&nbsp;&nbsp;<a href="https://github.com/ZERO-A-ONE"><img src="https://avatars.githubusercontent.com/ZERO-A-ONE?v=4" width="50px" alt="ZERO-A-ONE" /></a>&nbsp;&nbsp;</p>



## 🚀 Features

- 🌐 Internet access for searches and information gathering
- 💾 Long-term and short-term memory management
- 🧠 GPT-4 instances for text generation
- 🔗 Access to popular websites and platforms
- 🗃️ File storage and summarization with GPT-3.5
- 🔌 Extensibility with Plugins

## Quickstart

1. Get an OpenAI [API Key](https://platform.openai.com/account/api-keys)
2. Download the [latest release](https://github.com/Significant-Gravitas/Auto-GPT/releases/latest)
3. Follow the [installation instructions][docs/setup]
4. Configure any additional features you want, or install some [plugins][docs/plugins]
5. [Run][docs/usage] the app

Please see the [documentation][docs] for full setup instructions and configuration options.

[docs]: https://significant-gravitas.github.io/Auto-GPT/

## 📖 Documentation
* [⚙️ Setup][docs/setup]
* [💻 Usage][docs/usage]
* [🔌 Plugins][docs/plugins]
* Configuration
  * [🔍 Web Search](https://significant-gravitas.github.io/Auto-GPT/configuration/search/)
  * [🧠 Memory](https://significant-gravitas.github.io/Auto-GPT/configuration/memory/)
  * [🗣️ Voice (TTS)](https://significant-gravitas.github.io/Auto-GPT/configuration/voice/)
  * [🖼️ Image Generation](https://significant-gravitas.github.io/Auto-GPT/configuration/imagegen/)

[docs/setup]: https://significant-gravitas.github.io/Auto-GPT/setup/
[docs/usage]: https://significant-gravitas.github.io/Auto-GPT/usage/
[docs/plugins]: https://significant-gravitas.github.io/Auto-GPT/plugins/

## ⚠️ Limitations

This experiment aims to showcase the potential of GPT-4 but comes with some limitations:

1. Not a polished application or product, just an experiment
2. May not perform well in complex, real-world business scenarios. In fact, if it actually does, please share your results!
3. Quite expensive to run, so set and monitor your API key limits with OpenAI!

## 🛡 Disclaimer

This project, Auto-GPT, is an experimental application and is provided "as-is" without any warranty, express or implied. By using this software, you agree to assume all risks associated with its use, including but not limited to data loss, system failure, or any other issues that may arise.

The developers and contributors of this project do not accept any responsibility or liability for any losses, damages, or other consequences that may occur as a result of using this software. You are solely responsible for any decisions and actions taken based on the information provided by Auto-GPT.

**Please note that the use of the GPT-4 language model can be expensive due to its token usage.** By utilizing this project, you acknowledge that you are responsible for monitoring and managing your own token usage and the associated costs. It is highly recommended to check your OpenAI API usage regularly and set up any necessary limits or alerts to prevent unexpected charges.

As an autonomous experiment, Auto-GPT may generate content or take actions that are not in line with real-world business practices or legal requirements. It is your responsibility to ensure that any actions or decisions made based on the output of this software comply with all applicable laws, regulations, and ethical standards. The developers and contributors of this project shall not be held responsible for any consequences arising from the use of this software.

By using Auto-GPT, you agree to indemnify, defend, and hold harmless the developers, contributors, and any affiliated parties from and against any and all claims, damages, losses, liabilities, costs, and expenses (including reasonable attorneys' fees) arising from your use of this software or your violation of these terms.

## 🐦 Connect with Us on Twitter

Stay up-to-date with the latest news, updates, and insights about Auto-GPT by following our Twitter accounts. Engage with the developer and the AI's own account for interesting discussions, project updates, and more.

- **Developer**: Follow [@siggravitas](https://twitter.com/siggravitas) for insights into the development process, project updates, and related topics from the creator of Entrepreneur-GPT.
- **Entrepreneur-GPT**: Join the conversation with the AI itself by following [@En_GPT](https://twitter.com/En_GPT). Share your experiences, discuss the AI's outputs, and engage with the growing community of users.

We look forward to connecting with you and hearing your thoughts, ideas, and experiences with Auto-GPT. Join us on Twitter and let's explore the future of AI together!

<p align="center">
  <a href="https://star-history.com/#Torantulino/auto-gpt&Date">
    <img src="https://api.star-history.com/svg?repos=Torantulino/auto-gpt&type=Date" alt="Star History Chart">
  </a>
</p>
