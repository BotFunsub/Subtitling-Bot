<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center"> 
    <img src="images/botLogo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Subtitling Bot 
  </h3>
  <h3 align="center">
      机器人字幕组
  </h3>
  <p align="center">
        An ai tool to auto translating&subtitling your videos!
       <br />
        最好的支持四十种语言的在线字幕生成翻译工具
    <br />
    <a href="https://botfansub.tech"><strong>Explore the web »</strong></a>
        <a href="https://botfansub.tech/zh"><strong>网页版 »</strong></a>
    <br />
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://botfansub.tech)



工作流程:

* 输入视频/音频（mp4,mp3,wmbv......),选择模型，排队等待，下载翻译后的字幕(.srt).
* 语音转文字->文本翻译->添加每句台词的时间轴上位置
* 两个模型：语音转文字模型，翻译模型
* 弱监督语音转文字模型自带一定的翻译能力，在一些情况下将无需使用翻译模型

开源计划:
正在开发离线版本（linux/Windows）及命令行工具，这个仓库将用来上传开源的离线版本.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--Features -->
## Features

* Supports translation and recognition of over forty languages, we perform particularly well in niche languages!
* No need to install, generates online, without the hassle of environment configuration.
* Free and no registration required, we will distribute points based on server usage.
* Supports multiple models, free to choose between computing power and performance.

<br />

* 支持超四十种语言的翻译及识别，我们在小众语言表现尤其出色！
* 无需安装，在线生成，没有环境配置的烦恼.
* 免费且无需注册，我们会根据服务器使用情况发放积分.
* 支持多种模型，在算力和效果之间自由选择.

<!-- USAGE EXAMPLES -->
## Usage

### Web

We have a very good UI for web users, just follow the website, when you get the generated srt files, you have three options:

* You can use the srt file with video websites like Youtube, BiliBili...
* Use with media player like Windows Media Player, VLC Media Player, choose subtitles->your srt file.
* Want a video with embeded subtitles? instructions:

#### Use Ffmpeg:
1. Ffmpeg installation: <a href="https://ffmpeg.org"><strong>https://ffmpeg.org/</strong></a>
2. Use this command, remember replace input.mp4, input.srt and output.mp4:
  ```sh
   ffmpeg -i input.mp4 -vf "subtitles=input.srt" output.mp4
  ```    
#### Use web service

You can just google "embeded srt to video"

#### Why we do not offer to download the video with embeded generated subtitles?

It is currently free tool, and we cannot afford a server or cloud service for storing handreds of videos for a long period.


### Api

See our website,switch to the third option in the left side menu:

<a href="https://botfansub.tech"><strong>API »</strong></a>
<a href="https://botfansub.tech"><strong>中文版 »</strong></a>


<!-- CONTRIBUTING -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
