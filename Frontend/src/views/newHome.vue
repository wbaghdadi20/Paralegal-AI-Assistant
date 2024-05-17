<template>
  <div class="home">
    <div class="home-child" />
    <div class="questions">
      <b class="frequently-asked-questions">Frequently Asked Questions</b>
      <div class="question-1">
        <div class="question-1-child" />
        <b class="first-question">first question</b>
        <img class="frame-icon" alt="" src="@/assets/frame.svg" />
      </div>
      <div class="rectangle-parent">
        <div class="group-child" />
        <b class="second-question">second question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.svg" />
      </div>
      <div class="question-3">
        <div class="group-child" />
        <b class="second-question">third question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.svg" />
      </div>
      <div class="question-4">
        <div class="group-child" />
        <b class="second-question"> fourth question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.svg" />
      </div>
      <div class="question-5">
        <div class="group-child" />
        <b class="second-question">fifth question</b>
        <img class="frame-icon" alt="" src="@/assets/frame1.svg" />
      </div>
    </div>
    <div class="lets-get-in-touch">
      <b class="lets-get-in">Let’s Get in Touch</b>
      <div class="lets-get-in-touch-child" />
      <b class="email">email</b>
      <div class="lets-get-in-touch-item" />
      <div class="lets-get-in-touch-inner" />
      <b class="name">name</b>
      <b class="message">message</b>
      <input
        class="exampleemailcom"
        placeholder="example@email.com"
        type="text"
      />
      <input class="full-name" placeholder="full name" type="text" />
      <input
        class="write-your-message"
        placeholder="write your message...."
        type="text"
      />
      <button class="get-in-touch-wrapper">
        <b class="get-in-touch">Get in Touch</b>
      </button>
    </div>
    <div class="slogan">
      <b class="your-digital-legal-container">
        <p class="your-digital">Your Digital</p>
        <p class="your-digital">Legal Assistant</p>
        <p class="your-digital">Always Ready</p>
      </b>
      <div class="rectangle-group" @click="onGroupContainerClick">
        <button class="group-item" :autoFocus="true" />
        <button class="get-started" :autoFocus="true">Get Started</button>
      </div>
    </div>
    <div class="sign-in-sign-up1">
      <button class="sign-in1" :autoFocus="true" @click="onSignInClick">
        Sign In
      </button>
      <button class="sign-up2" :autoFocus="true" @click="onSignUpClick">
        <div class="sign-up-item" />
        <button class="sign-up3" :autoFocus="true">Sign Up</button>
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
      <div class="rectangle-container">
        <div class="group-inner" />
        <div class="rectangle-div" />
        <b class="services">Services</b>
        <div class="blah1">blah</div>
        <b class="b">50</b>
        <div class="mo">/mo</div>
        <div class="group-parent">
          <div class="parent">
            <div class="div">1</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
          <div class="group">
            <div class="div">2</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
          <div class="container">
            <div class="div">3</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
        </div>
        <div class="group-container">
          <div class="group-div">
            <div class="div">4</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
          <div class="group">
            <div class="div">5</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
          <div class="parent2">
            <div class="div">6</div>
            <img class="frame-icon5" alt="" src="@/assets/frame2.svg" />
          </div>
        </div>
        <img class="frame-icon11" alt="" src="@/assets/frame3.svg" />
      </div>
    </div>
    <div class="top-bar">
      <div class="top-bar-child" />
      <button class="home1">Home</button>
      <button class="about" :autoFocus="true" :onClick="onAboutClick">
        About
      </button>
      <button class="how-it-works" :autoFocus="true">How it Works</button>
      <button class="service" :autoFocus="true">Service</button>
      <button class="about-us" :autoFocus="true">About Us</button>
    </div>
    <div class="what-we-do">
      <b class="what-we-do1" data-scroll-to="whatWeDo">What We do</b>
      <div class="frame-parent">
        <div class="first-wrapper">
          <div class="first">first</div>
        </div>
        <div class="first-wrapper">
          <div class="first">second</div>
        </div>
        <div class="first-wrapper">
          <div class="first">third</div>
        </div>
      </div>
    </div>
    <div class="logo-top1">
      <b class="themis-ai1">THEMIS AI</b>
      <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
    </div>
    <div class="bottom-contact-information">
      <div class="bottom-contact-information-child" />
      <div class="basic-info">basic info</div>
      <div class="home-parent">
        <div class="home2">Home</div>
        <div class="about1">About</div>
        <div class="how-it-works1">How it Works</div>
        <div class="services1">Services</div>
      </div>
      <div class="logo-bottom">
        <b class="themis-ai2">THEMIS AI</b>
        <img class="logo-1-icon2" alt="" src="@/assets/logo.png" />
      </div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Home",
    methods: {
      onGroupContainerClick() {
        this.$router.push("/");
      },
      onSignInClick() {
        // Please sync "sign in" to the project
      },
      onSignUpClick() {
        // Please sync "sign up" to the project
      },
      onAboutClick() {
        const anchor = document.querySelector("[data-scroll-to='whatWeDo']");
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
    color: var(--color-white);
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
    font-size: var(--font-size-lg);
    color: var(--color-gray-100);
  }
  .lets-get-in {
    position: absolute;
    top: calc(50% - 360px);
    left: calc(50% - 250px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .lets-get-in-touch-child {
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
  .lets-get-in-touch-item {
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
  .lets-get-in-touch-inner {
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
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 195px;
    left: 32px;
    line-height: 150%;
    color: var(--color-lightslategray);
    text-align: left;
  }
  .full-name {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 313px;
    left: 32px;
    line-height: 150%;
    color: var(--color-lightslategray);
    text-align: left;
  }
  .write-your-message {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 431px;
    left: 32px;
    line-height: 150%;
    color: var(--color-lightslategray);
    text-align: left;
  }
  .get-in-touch {
    position: absolute;
    top: 19px;
    left: 301px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-family: var(--font-raleway);
    color: var(--color-darkslategray);
    text-align: center;
  }
  .get-in-touch-wrapper {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: var(--color-white);
    position: absolute;
    height: 8.61%;
    width: 100%;
    top: 91.39%;
    right: 0%;
    bottom: 0%;
    left: 0%;
    border-radius: var(--br-3xs);
    overflow: hidden;
  }
  .lets-get-in-touch {
    position: absolute;
    top: calc(50% + 1292.5px);
    left: calc(50% - 348px);
    width: 696px;
    height: 720px;
    font-size: var(--font-size-lg);
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
  .group-item {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: var(--color-white);
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
    color: var(--color-darkslategray);
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
  }
  .sign-in1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 12px;
    left: 0px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: left;
    display: inline-block;
    opacity: 0.8;
  }
  .sign-up-item {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-white);
    width: 132px;
    height: 48px;
  }
  .sign-up3 {
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
    color: var(--color-darkslategray);
    text-align: center;
    display: inline-block;
    width: 60px;
  }
  .sign-up2 {
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
  .sign-in-sign-up1 {
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
  .group-inner {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-xl);
    background-color: #f8f8f8;
    width: 624px;
    height: 497px;
    mix-blend-mode: linear-dodge;
  }
  .rectangle-div {
    position: absolute;
    top: 345px;
    left: 22px;
    border-radius: var(--br-3xs);
    background-color: #f5f8ff;
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
    left: 419px;
    width: 624px;
    height: 497px;
    font-size: var(--font-size-sm);
    color: var(--color-gray-100);
    font-family: var(--paragraph);
  }
  .pricing {
    position: absolute;
    top: calc(50% - 94.5px);
    left: calc(50% - 507px);
    width: 1043px;
    height: 497px;
  }
  .top-bar-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-xl);
    background-color: rgba(255, 255, 255, 0.6);
    border: 1px solid var(--color-white);
    box-sizing: border-box;
    width: 607px;
    height: 68px;
  }
  .home1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 57px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
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
    left: 150px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
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
    left: 244px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--paragraph);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .service {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 389px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .about-us {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 22px;
    left: 482px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
  }
  .top-bar {
    position: absolute;
    top: 19px;
    left: 417px;
    width: 607px;
    height: 68px;
  }
  .what-we-do1 {
    position: absolute;
    top: calc(50% - 274.5px);
    left: calc(50% - 502.5px);
    line-height: 120%;
  }
  .first {
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
    width: 100%;
    top: 98px;
    right: 0px;
    left: 0px;
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
  .what-we-do {
    position: absolute;
    top: calc(50% - 2027.5px);
    left: calc(50% - 691px);
    width: 1171px;
    height: 549px;
  }
  .themis-ai1 {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
  }
  .logo-1-icon1 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
  }
  .logo-top1 {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
    text-align: center;
    font-size: var(--font-size-xl);
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
  .services1 {
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
  .themis-ai2 {
    position: absolute;
    top: 36px;
    left: 63.6px;
    line-height: 150%;
    display: inline-block;
    width: 255.4px;
    height: 37.2px;
  }
  .logo-1-icon2 {
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
  .home {
    width: 100%;
    position: relative;
    background-color: var(--color-darkslategray);
    height: 5371px;
    overflow: hidden;
    text-align: left;
    font-size: var(--font-size-41xl);
    color: var(--color-white);
    font-family: var(--font-raleway);
  }
</style>
