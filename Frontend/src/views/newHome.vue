<template>
  <div class="home">
    <img class="home-child" alt="" />
    <img class="mask-group-icon" alt="" src="@/assets/mask-group@2x.png" />
    <div class="home-item" />
    <div class="questions">
      <b class="frequently-asked-questions">Frequently Asked Questions</b>
      <div class="question-1">
        <div class="question-1-child" />
        <b class="first-question">first question</b>
        <img class="frame-icon" alt="" src="@/assets/frame.png" />
      </div>
      <div class="question-2">
        <div class="rectangle-parent">
          <div class="group-child" />
          <b class="second-question">second question</b>
          <img class="frame-icon" alt="" src="@/assets/frame1.png" />
        </div>
      </div>
      <div class="question-3">
        <div class="group-child" />
        <b class="second-question">third question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.png" />
      </div>
      <div class="question-4">
        <div class="group-child" />
        <b class="second-question"> fourth question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.png" />
      </div>
      <div class="question-5">
        <div class="group-child" />
        <b class="second-question">fifth question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.png" />
      </div>
    </div>
    <div class="lets-get-in-touch">
      <div class="lets-get-in-touch-parent">
        <b class="lets-get-in">Let’s Get in Touch</b>
        <div class="group-item" />
        <b class="email">email</b>
        <div class="group-inner" />
        <div class="rectangle-div" />
        <b class="name">name</b>
        <b class="message">message</b>
        <div class="exampleemailcom">example@email.com</div>
        <div class="full-name">full name</div>
        <div class="write-your-message">write your message....</div>
        <div class="get-in-touch-wrapper">
          <b class="get-in-touch">Get in Touch</b>
        </div>
      </div>
    </div>
    <div class="slogan">
      <b class="your-digital-legal-container">
        <p class="your-digital">Your Digital</p>
        <p class="your-digital">Legal Assistant</p>
        <p class="your-digital">Always Ready</p>
      </b>
      <div class="rectangle-group" @click="onGroupContainerClick">
        <button class="rectangle-button" :autoFocus="true" />
        <button class="get-started" :autoFocus="true">Get Started</button>
      </div>
    </div>
    <div class="sign-in-sign-up">
      <button class="sign-in" :autoFocus="true">Sign In</button>
      <button class="sign-up" :autoFocus="true">
        <div class="sign-up-child" />
        <button class="sign-up1" :autoFocus="true">Sign Up</button>
      </button>
    </div>
    <div class="check-our-work">
      <b class="check-our-work1">Check our Work</b>
    </div>
    <div class="pricing">
      <div class="pricing-slogon">
        <b class="pricing1">Pricing</b>
        <div class="blah">blah</div>
      </div>
      <div class="pricing-block">
        <div class="rectangle-container">
          <div class="group-child1" />
          <div class="group-child2" />
          <b class="services">Services</b>
          <div class="blah1">blah</div>
          <b class="b">50</b>
          <div class="mo">/mo</div>
          <div class="group-parent">
            <div class="parent">
              <div class="div">1</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
            <div class="group">
              <div class="div">2</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
            <div class="container">
              <div class="div">3</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
          </div>
          <div class="group-container">
            <div class="group-div">
              <div class="div">4</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
            <div class="group">
              <div class="div">5</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
            <div class="parent2">
              <div class="div">6</div>
              <img class="frame-icon5" alt="" src="@/assets/frame2.png" />
            </div>
          </div>
          <img class="frame-icon11" alt="" src="@/assets/frame3.png" />
        </div>
      </div>
    </div>
    <div class="top-bar">
      <div class="top-bar-child" />
      <button class="home1">Home</button>
      <button class="about" :autoFocus="true" :onClick="onAboutClick">
        About
      </button>
      <button class="how-it-works" :autoFocus="true">How it Works</button>
      <button class="services1" :autoFocus="true" :onClick="onServicesClick">
        Services
      </button>
    </div>
    <div class="what-we-do">
      <b class="what-we-do1" data-scroll-to="whatWeDo">What We do</b>
      <div class="what-we-do-block-1">
        <div class="what-we-do-block-1-child" />
        <div class="first">first</div>
        <div class="blah2">blah</div>
        <div class="what-we-do-block-1-item" />

      </div>
      <div class="what-we-do-block-2">
        <div class="what-we-do-block-1-child" />
        <div class="second">Second</div>
        <div class="blah3">blah</div>
        <div class="what-we-do-block-2-inner">
          <div class="group-child3" />
        </div>

      </div>
      <div class="what-we-do-block-3">
        <div class="what-we-do-block-1-child" />
        <div class="third">Third</div>
        <div class="blah4">blah</div>
        <div class="what-we-do-block-3-inner">
          <div class="group-child3" />
        </div>

      </div>
      <div class="what-we-do-block-4">
        <div class="what-we-do-block-4-child" />
        <div class="forth">Forth</div>
        <div class="blah5">blah</div>
        <div class="what-we-do-block-4-inner">
          <div class="group-child3" />
        </div>

      </div>
    </div>
    <div class="logo-top">
      <b class="themis-ai">THEMIS AI</b>
      <img class="logo-1-icon" alt="" src="@/assets/logo.png" />
    </div>
    <div class="bottom-contact-information">
      <div
        class="bottom-contact-information-child"
        data-scroll-to="rectangle"
      />
      <div class="basic-info">basic info</div>
      <div class="home-parent">
        <div class="home2">Home</div>
        <div class="about1">About</div>
        <div class="how-it-works1">How it Works</div>
        <div class="services2">Services</div>
      </div>
      <div class="logo-bottom">
        <b class="themis-ai1">THEMIS AI</b>
        <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
      </div>
    </div>
    <div class="frame-parent">
      <div class="first-wrapper">
        <div class="first1">first</div>
      </div>
      <div class="first-wrapper">
        <div class="first1">second</div>
      </div>
      <div class="first-wrapper">
        <div class="first1">third</div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Home",
    methods: {
      onGroupContainerClick() {
        this.$router.push("/ai-system");
      },
      onAboutClick() {
        const anchor = document.querySelector("[data-scroll-to='whatWeDo']");
        if (anchor) {
          anchor.scrollIntoView({ block: "start", behavior: "smooth" });
        }
      },
      onServicesClick() {
        const anchor = document.querySelector("[data-scroll-to='rectangle']");
        if (anchor) {
          anchor.scrollIntoView({ block: "start", behavior: "smooth" });
        }
      },
    },
  });
</script>
<style scoped>
  .home-child {
    position: absolute;
    height: 6.98%;
    width: 210.86%;
    top: 98.32%;
    right: -67.15%;
    bottom: -5.3%;
    left: -43.71%;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    display: none;
  }
  .mask-group-icon {
    position: absolute;
    height: 21.55%;
    width: 81.13%;
    top: -4.36%;
    right: 9.41%;
    bottom: 82.8%;
    left: 9.47%;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: contain;
    display: none;
  }
  .home-item {
    position: absolute;
    top: 3853.5px;
    left: -0.5px;
    border-top: 1px solid var(--color-lavender);
    box-sizing: border-box;
    width: 1441px;
    height: 1px;
  }
  .frequently-asked-questions {
    position: absolute;
    top: calc(50% - 143.5px);
    left: calc(50% - 573.5px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
    display: inline-block;
    width: 454px;
  }
  .question-1-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background: linear-gradient(121.9deg, #1c1c1c, #050505);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 696px;
    height: 137px;
    mix-blend-mode: linear-dodge;
  }
  .first-question {
    position: absolute;
    top: calc(50% - 44.5px);
    left: calc(50% - 318px);
    line-height: 120%;
  }
  .frame-icon {
    position: absolute;
    top: 23px;
    left: 655px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .question-1 {
    position: absolute;
    top: 0px;
    left: 451px;
    width: 696px;
    height: 137px;
  }
  .group-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background: linear-gradient(121.9deg, #1c1c1c, #050505);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: linear-dodge;
  }
  .second-question {
    position: absolute;
    top: calc(50% - 11px);
    left: calc(50% - 318px);
    line-height: 120%;
  }
  .rectangle-parent {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 696px;
    height: 70px;
  }
  .question-2 {
    position: absolute;
    top: 153px;
    left: 451px;
    width: 696px;
    height: 70px;
  }
  .question-3 {
    position: absolute;
    top: 239px;
    left: 451px;
    width: 696px;
    height: 70px;
  }
  .question-4 {
    position: absolute;
    top: 325px;
    left: 451px;
    width: 696px;
    height: 70px;
  }
  .question-5 {
    position: absolute;
    top: 411px;
    left: 451px;
    width: 696px;
    height: 70px;
  }
  .questions {
    position: absolute;
    top: calc(50% + 576.5px);
    left: calc(50% - 539px);
    width: 1147px;
    height: 481px;
  }
  .lets-get-in {
    position: absolute;
    top: calc(50% - 360px);
    left: calc(50% - 252px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .group-item {
    position: absolute;
    top: 175px;
    left: 0px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-lavender);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .email {
    position: absolute;
    top: calc(50% - 217px);
    left: calc(50% - 341px);
    line-height: 120%;
  }
  .group-inner {
    position: absolute;
    top: 293px;
    left: 0px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-lavender);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .rectangle-div {
    position: absolute;
    top: 411px;
    left: 0px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-lavender);
    box-sizing: border-box;
    width: 696px;
    height: 222px;
    mix-blend-mode: normal;
  }
  .name {
    position: absolute;
    top: calc(50% - 99px);
    left: calc(50% - 341px);
    line-height: 120%;
  }
  .message {
    position: absolute;
    top: calc(50% + 19px);
    left: calc(50% - 341px);
    line-height: 120%;
  }
  .exampleemailcom {
    position: absolute;
    top: 195px;
    left: 32px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    color: var(--color-lightslategray);
  }
  .full-name {
    position: absolute;
    top: 313px;
    left: 32px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    color: var(--color-lightslategray);
  }
  .write-your-message {
    position: absolute;
    top: 431px;
    left: 32px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    color: var(--color-lightslategray);
  }
  .get-in-touch {
    position: absolute;
    top: 19px;
    left: 301px;
    line-height: 150%;
  }
  .get-in-touch-wrapper {
    position: absolute;
    height: 8.61%;
    width: 100%;
    top: 91.39%;
    right: 0%;
    bottom: 0%;
    left: 0%;
    border-radius: var(--br-3xs);
    background-color: var(--color-darkslategray);
    overflow: hidden;
    text-align: center;
    font-size: var(--paragraph-size);
    color: var(--color-white);
    font-family: var(--font-raleway);
  }
  .lets-get-in-touch-parent {
    position: absolute;
    top: calc(50% - 360px);
    left: calc(50% - 348px);
    width: 696px;
    height: 720px;
  }
  .lets-get-in-touch {
    position: absolute;
    top: calc(50% + 1292.5px);
    left: calc(50% - 348px);
    width: 696px;
    height: 720px;
    font-family: var(--paragraph);
  }
  .your-digital {
    margin: 0;
  }
  .your-digital-legal-container {
    position: absolute;
    top: calc(50% - 157.5px);
    left: calc(50% - 504.5px);
    line-height: 100%;
    display: inline-block;
    width: 1009px;
    height: 229px;
  }
  .rectangle-button {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: var(--color-darkslategray);
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    width: 211px;
    height: 60px;
  }
  .get-started {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 18px;
    left: 61px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
  }
  .rectangle-group {
    position: absolute;
    top: 255px;
    left: 400px;
    width: 211px;
    height: 60px;
    cursor: pointer;
  }
  .slogan {
    position: absolute;
    top: calc(50% - 2496.5px);
    left: calc(50% - 505px);
    width: 1009px;
    height: 315px;
    text-align: center;
    font-size: 73.3px;
    color: var(--color-darkslategray);
  }
  .sign-in {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 12px;
    left: 0px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--font-raleway);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
    opacity: 0.8;
  }
  .sign-up-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-darkslategray);
    width: 132px;
    height: 48px;
  }
  .sign-up1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 12px;
    left: 36px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
    width: 60px;
  }
  .sign-up {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 0px;
    left: 69px;
    width: 132px;
    height: 48px;
  }
  .sign-in-sign-up {
    position: absolute;
    top: 26px;
    left: 1127px;
    width: 201px;
    height: 48px;
  }
  .check-our-work-pic {
    position: absolute;
    top: -87px;
    left: calc(50% - 399.5px);
    width: 799px;
    height: 841px;
    object-fit: cover;
    display: none;
    mix-blend-mode: color-burn;
  }
  .check-our-work1 {
    position: absolute;
    top: calc(50% - 36px);
    left: calc(50% - 227.5px);
    line-height: 120%;
  }
  .check-our-work {
    position: absolute;
    top: 1458px;
    left: calc(50% - 227px);
    width: 455px;
    height: 72px;
    font-size: var(--font-size-41xl);
  }
  .pricing1 {
    position: absolute;
    top: calc(50% - 54.5px);
    left: calc(50% - 141px);
    line-height: 120%;
  }
  .blah {
    position: absolute;
    top: 88px;
    left: 0px;
    font-size: var(--font-size-sm);
    line-height: 150%;
    font-family: var(--paragraph);
    color: var(--color-lightslategray);
    display: inline-block;
    width: 282px;
  }
  .pricing-slogon {
    position: absolute;
    top: calc(50% - 221.5px);
    left: calc(50% - 521.5px);
    width: 282px;
    height: 109px;
  }
  .group-child1 {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-xl);
    background-color: #4e47ff;
    width: 624px;
    height: 497px;
    mix-blend-mode: linear-dodge;
  }
  .group-child2 {
    position: absolute;
    top: 345px;
    left: 22px;
    border-radius: var(--br-3xs);
    background-color: var(--color-ghostwhite);
    width: 579px;
    height: 127px;
    mix-blend-mode: normal;
  }
  .services {
    position: absolute;
    top: calc(50% - 205.5px);
    left: calc(50% - 262px);
    font-size: var(--font-size-11xl);
    line-height: 120%;
    font-family: var(--font-raleway);
  }
  .blah1 {
    position: absolute;
    top: 110px;
    left: 50px;
    line-height: 150%;
    color: var(--color-lightslategray);
    display: inline-block;
    width: 383px;
  }
  .b {
    position: absolute;
    top: calc(50% + 124.5px);
    left: calc(50% - 248px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
  }
  .mo {
    position: absolute;
    top: 409px;
    left: 148px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    color: var(--color-lightslategray);
  }
  .div {
    position: absolute;
    top: 0px;
    left: 37px;
    line-height: 180%;
  }
  .frame-icon5 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .parent {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 44px;
    height: 25px;
  }
  .group {
    position: absolute;
    top: 43px;
    left: 0px;
    width: 46px;
    height: 25px;
  }
  .container {
    position: absolute;
    top: 86px;
    left: 0px;
    width: 50px;
    height: 25px;
  }
  .group-parent {
    position: absolute;
    top: 193px;
    left: 50px;
    width: 50px;
    height: 111px;
  }
  .group-div {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 46px;
    height: 25px;
  }
  .parent2 {
    position: absolute;
    top: 86px;
    left: 0px;
    width: 46px;
    height: 25px;
  }
  .group-container {
    position: absolute;
    top: 193px;
    left: 331px;
    width: 46px;
    height: 111px;
  }
  .frame-icon11 {
    position: absolute;
    top: 400px;
    left: 531px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .rectangle-container {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 624px;
    height: 497px;
  }
  .pricing-block {
    position: absolute;
    top: 0px;
    left: 419px;
    width: 624px;
    height: 497px;
    font-size: var(--font-size-sm);
    font-family: var(--paragraph);
  }
  .pricing {
    position: absolute;
    top: calc(50% - 94.5px);
    left: calc(50% - 507px);
    width: 1043px;
    height: 497px;
    font-size: var(--font-size-41xl);
  }
  .top-bar-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-xl);
    background-color: var(--color-gray-200);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 499px;
    height: 68px;
  }
  .home1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 56px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--paragraph);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .about {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 149px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--paragraph);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .how-it-works {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 243px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--paragraph);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .services1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 391px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--paragraph);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .top-bar {
    position: absolute;
    top: 16px;
    left: 471px;
    width: 499px;
    height: 68px;
  }
  .what-we-do1 {
    position: absolute;
    top: calc(50% - 178px);
    left: calc(50% - 608px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
    font-family: var(--font-raleway);
  }
  .what-we-do-block-1-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background: linear-gradient(121.9deg, #1c1c1c, #050505);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 280px;
    height: 252px;
    mix-blend-mode: linear-dodge;
  }
  .first {
    position: absolute;
    top: calc(50% - 34px);
    left: calc(50% - 114px);
    line-height: 120%;
    font-weight: 600;
  }
  .blah2 {
    position: absolute;
    top: 134px;
    left: 26px;
    font-size: var(--font-size-sm);
    line-height: 150%;
    color: var(--color-lightslategray);
    display: inline-block;
    width: 231px;
  }
  .what-we-do-block-1-item {
    position: absolute;
    top: 29px;
    left: 26px;
    border-radius: var(--br-4xs);
    background-color: var(--color-ghostwhite);
    width: 44px;
    height: 44px;
    mix-blend-mode: normal;
  }
  .block1-icon {
    position: absolute;
    top: 39px;
    left: 36px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .what-we-do-block-1 {
    position: absolute;
    top: 104px;
    left: 0px;
    width: 280px;
    height: 252px;
  }
  .second {
    position: absolute;
    top: calc(50% - 34px);
    left: calc(50% - 116px);
    line-height: 120%;
    font-weight: 600;
  }
  .blah3 {
    position: absolute;
    top: 134px;
    left: 24px;
    font-size: var(--font-size-sm);
    line-height: 150%;
    color: var(--color-lightslategray);
    display: inline-block;
    width: 231px;
  }
  .group-child3 {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-4xs);
    background-color: var(--color-ghostwhite);
    width: 44px;
    height: 44px;
  }
  .what-we-do-block-2-inner {
    position: absolute;
    top: 29px;
    left: 24px;
    width: 44px;
    height: 44px;
  }
  .frame-icon12 {
    position: absolute;
    top: 39px;
    left: 34px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .what-we-do-block-2 {
    position: absolute;
    top: 104px;
    left: 312px;
    width: 280px;
    height: 252px;
  }
  .third {
    position: absolute;
    top: calc(50% - 34px);
    left: calc(50% - 118px);
    line-height: 120%;
    font-weight: 600;
  }
  .blah4 {
    position: absolute;
    top: 134px;
    left: 22px;
    font-size: var(--font-size-sm);
    line-height: 150%;
    color: var(--color-lightslategray);
    display: inline-block;
    width: 231px;
  }
  .what-we-do-block-3-inner {
    position: absolute;
    top: 29px;
    left: 22px;
    width: 44px;
    height: 44px;
  }
  .frame-icon13 {
    position: absolute;
    top: 40px;
    left: 32px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .what-we-do-block-3 {
    position: absolute;
    top: 104px;
    left: 624px;
    width: 280px;
    height: 252px;
  }
  .what-we-do-block-4-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background: linear-gradient(121.9deg, #1c1c1c, #050505);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 289px;
    height: 252px;
    mix-blend-mode: linear-dodge;
  }
  .forth {
    position: absolute;
    top: calc(50% - 34px);
    left: calc(50% - 115.5px);
    line-height: 120%;
    font-weight: 600;
  }
  .blah5 {
    position: absolute;
    top: 134px;
    left: 29px;
    font-size: var(--font-size-sm);
    line-height: 150%;
    color: var(--color-lightslategray);
    display: inline-block;
    width: 231px;
  }
  .what-we-do-block-4-inner {
    position: absolute;
    top: 29px;
    left: 29px;
    width: 44px;
    height: 44px;
  }
  .frame-icon14 {
    position: absolute;
    top: 39px;
    left: 39px;
    width: 24px;
    height: 24px;
    overflow: hidden;
  }
  .what-we-do-block-4 {
    position: absolute;
    top: 104px;
    left: 927px;
    width: 289px;
    height: 252px;
  }
  .what-we-do {
    position: absolute;
    top: calc(50% - 2027.5px);
    left: calc(50% - 608px);
    width: 1216px;
    height: 356px;
    font-size: var(--font-size-lgi-8);
    font-family: var(--paragraph);
  }
  .themis-ai {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
  }
  .logo-1-icon {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
  }
  .logo-top {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
    text-align: center;
    font-size: var(--font-size-xl);
    color: var(--color-black);
  }
  .bottom-contact-information-child {
    position: absolute;
    top: 0px;
    left: calc(50% - 608px);
    border-radius: 40px;
    background: linear-gradient(121.9deg, #fff, #f7f9ff);
    border: 1px solid var(--color-lavender);
    box-sizing: border-box;
    width: 1216px;
    height: 398px;
    mix-blend-mode: normal;
  }
  .basic-info {
    position: absolute;
    top: 163px;
    left: calc(50% - 536px);
    line-height: 150%;
    display: inline-block;
    width: 356px;
  }
  .home2 {
    position: absolute;
    top: 0px;
    left: 0px;
    line-height: 150%;
  }
  .about1 {
    position: absolute;
    top: 0px;
    left: 93px;
    line-height: 150%;
  }
  .how-it-works1 {
    position: absolute;
    top: 0px;
    left: 187px;
    line-height: 150%;
  }
  .services2 {
    position: absolute;
    top: 0px;
    left: 335px;
    line-height: 150%;
  }
  .home-parent {
    position: absolute;
    top: 155px;
    left: 743px;
    width: 401px;
    height: 24px;
  }
  .themis-ai1 {
    position: absolute;
    top: 36px;
    left: 63.6px;
    line-height: 150%;
    display: inline-block;
    width: 255.4px;
    height: 37.2px;
  }
  .logo-1-icon1 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 105px;
    height: 113px;
    object-fit: cover;
  }
  .logo-bottom {
    position: absolute;
    top: 26px;
    left: 72px;
    width: 319px;
    height: 113px;
    text-align: center;
    font-size: var(--font-size-11xl);
    color: var(--color-black);
    font-family: var(--font-raleway);
  }
  .bottom-contact-information {
    position: absolute;
    top: 4854px;
    left: calc(50% - 608px);
    width: 1216px;
    height: 398px;
    font-size: var(--paragraph-size);
    color: var(--color-lightslategray);
    font-family: var(--paragraph);
  }
  .first1 {
    position: relative;
  }
  .first-wrapper {
    border-radius: var(--br-3xs);
    background-color: var(--color-white);
    border: 3px solid var(--color-darkslategray);
    overflow: hidden;
    flex-shrink: 0;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-176xl) var(--padding-457xl);
  }
  .frame-parent {
    position: absolute;
    width: calc(100% - 269px);
    top: 1660px;
    right: 159px;
    left: 110px;
    overflow-x: auto;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 0px 56px;
    box-sizing: border-box;
    gap: 68px;
    font-size: var(--font-size-31xl);
    color: var(--color-black);
    font-family: var(--paragraph);
  }
  .home {
    width: 100%;
    position: relative;
    background-color: var(--color-ghostwhite);
    height: 5371px;
    overflow: hidden;
    text-align: left;
    font-size: var(--font-size-lg);
    color: var(--color-gray-100);
    font-family: var(--font-raleway);
  }
</style>
