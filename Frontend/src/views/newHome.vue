<template>
    <div :class="$style.home">
      <img :class="$style.homeChild" alt="" />
      <div :class="$style.homeItem" />
      <div :class="$style.questions">
        <b :class="$style.frequentlyAskedQuestions">Frequently Asked Questions</b>
        <div :class="$style.question1">
          <div :class="$style.question1Child" />
          <b :class="$style.firstQuestion">first question</b>
          <img :class="$style.frameIcon" alt="" src="@/assets/frame.png" />
        </div>
        <div :class="$style.question2">
          <div :class="$style.rectangleParent">
            <div :class="$style.groupChild" />
            <b :class="$style.secondQuestion">second question</b>
            <img :class="$style.frameIcon" alt="" src="@/assets/frame1.png" />
          </div>
        </div>
        <div :class="$style.question3">
          <div :class="$style.groupChild" />
          <b :class="$style.secondQuestion">third question</b>
          <img :class="$style.frameIcon" alt="" src="@/assets/frame1.png" />
        </div>
        <div :class="$style.question4">
          <div :class="$style.groupChild" />
          <b :class="$style.secondQuestion"> fourth question</b>
          <img :class="$style.frameIcon" alt="" src="@/assets/frame1.png" />
        </div>
        <div :class="$style.question5">
          <div :class="$style.groupChild" />
          <b :class="$style.secondQuestion">fifth question</b>
          <img :class="$style.frameIcon" alt="" src="@/assets/frame1.png" />
        </div>
      </div>
      <div :class="$style.letsGetInTouch">
        <div :class="$style.letsGetInTouchParent">
          <b :class="$style.letsGetIn">Let’s Get in Touch</b>
          <div :class="$style.groupItem" />
          <b :class="$style.email">email</b>
          <div :class="$style.groupInner" />
          <div :class="$style.rectangleDiv" />
          <b :class="$style.name">name</b>
          <b :class="$style.message">message</b>
          <div :class="$style.exampleemailcom">example@email.com</div>
          <div :class="$style.fullName">full name</div>
          <div :class="$style.writeYourMessage">write your message....</div>
          <div :class="$style.getInTouchWrapper">
            <b :class="$style.getInTouch">Get in Touch</b>
          </div>
        </div>
      </div>
      <div :class="$style.slogan">
        <b :class="$style.yourDigitalLegalContainer">
          <p :class="$style.yourDigital">Your Digital</p>
          <p :class="$style.yourDigital">Legal Assistant</p>
          <p :class="$style.yourDigital">Always Ready</p>
        </b>
        <div :class="$style.rectangleGroup" @click="onGroupContainerClick">
          <button :class="$style.rectangleButton" :autoFocus="true" />
          <button :class="$style.getStarted" :autoFocus="true">
            Get Started
          </button>
        </div>
      </div>
      <div :class="$style.signInSignUp">
        <button :class="$style.signIn" :autoFocus="true">Sign In</button>
        <button :class="$style.signUp" :autoFocus="true">
          <div :class="$style.signUpChild" />
          <button :class="$style.signUp1" :autoFocus="true">Sign Up</button>
        </button>
      </div>
      <div :class="$style.checkOurWork">
        <b :class="$style.checkOurWork1">Check our Work</b>
      </div>
      <div :class="$style.pricing">
        <div :class="$style.pricingSlogon">
          <b :class="$style.pricing1">Pricing</b>
          <div :class="$style.blah">blah</div>
        </div>
        <div :class="$style.pricingBlock">
          <div :class="$style.rectangleContainer">
            <div :class="$style.groupChild1" />
            <div :class="$style.groupChild2" />
            <b :class="$style.services">Services</b>
            <div :class="$style.blah1">blah</div>
            <b :class="$style.b">50</b>
            <div :class="$style.mo">/mo</div>
            <div :class="$style.groupParent">
              <div :class="$style.parent">
                <div :class="$style.div">1</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
              <div :class="$style.group">
                <div :class="$style.div">2</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
              <div :class="$style.container">
                <div :class="$style.div">3</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
            </div>
            <div :class="$style.groupContainer">
              <div :class="$style.groupDiv">
                <div :class="$style.div">4</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
              <div :class="$style.group">
                <div :class="$style.div">5</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
              <div :class="$style.parent2">
                <div :class="$style.div">6</div>
                <img :class="$style.frameIcon5" alt="" src="@/assets/frame2.png" />
              </div>
            </div>
            <img :class="$style.frameIcon11" alt="" src="@/assets/frame3.png" />
          </div>
        </div>
      </div>
      <div :class="$style.topBar">
        <div :class="$style.topBarChild" />
        <button :class="$style.home1">Home</button>
        <button :class="$style.about" :autoFocus="true" :onClick="onAboutClick">
          About
        </button>
        <button :class="$style.howItWorks" :autoFocus="true">How it Works</button>
        <button
          :class="$style.services1"
          :autoFocus="true"
          :onClick="onServicesClick"
        >
          Services
        </button>
      </div>
      <div :class="$style.whatWeDo">
        <b :class="$style.whatWeDo1" data-scroll-to="whatWeDo">What We do</b>
        <div :class="$style.whatWeDoBlock1">
          <div :class="$style.whatWeDoBlock1Child" />
          <div :class="$style.first">first</div>
          <div :class="$style.blah2">blah</div>
          <div :class="$style.whatWeDoBlock1Item" />

        </div>
        <div :class="$style.whatWeDoBlock2">
          <div :class="$style.whatWeDoBlock1Child" />
          <div :class="$style.second">Second</div>
          <div :class="$style.blah3">blah</div>
          <div :class="$style.whatWeDoBlock2Inner">
            <div :class="$style.groupChild3" />
          </div>

        </div>
        <div :class="$style.whatWeDoBlock3">
          <div :class="$style.whatWeDoBlock1Child" />
          <div :class="$style.third">Third</div>
          <div :class="$style.blah4">blah</div>
          <div :class="$style.whatWeDoBlock3Inner">
            <div :class="$style.groupChild3" />
          </div>

        </div>
        <div :class="$style.whatWeDoBlock4">
          <div :class="$style.whatWeDoBlock4Child" />
          <div :class="$style.forth">Forth</div>
          <div :class="$style.blah5">blah</div>
          <div :class="$style.whatWeDoBlock4Inner">
            <div :class="$style.groupChild3" />
          </div>

        </div>
      </div>
      <div :class="$style.logoTop">
        <b :class="$style.themisAi">THEMIS AI</b>
        <img :class="$style.logo1Icon" alt="" src="@/assets/logo.png" />
      </div>
      <div :class="$style.bottomContactInformation">
        <div
          :class="$style.bottomContactInformationChild"
          data-scroll-to="rectangle"
        />
        <div :class="$style.basicInfo">basic info</div>
        <div :class="$style.homeParent">
          <div :class="$style.home2">Home</div>
          <div :class="$style.about1">About</div>
          <div :class="$style.howItWorks1">How it Works</div>
          <div :class="$style.services2">Services</div>
        </div>
        <div :class="$style.logoBottom">
          <b :class="$style.themisAi1">THEMIS AI</b>
          <img :class="$style.logo1Icon1" alt="" src="@/assets/logo.png" />
        </div>
      </div>
      <div :class="$style.frameParent">
        <div :class="$style.firstWrapper">
          <div :class="$style.first1">first</div>
        </div>
        <div :class="$style.firstWrapper">
          <div :class="$style.first1">second</div>
        </div>
        <div :class="$style.firstWrapper">
          <div :class="$style.first1">third</div>
        </div>
      </div>
    </div>
  </template>
  <script lang="ts">
    import { User as UserIcon } from '@element-plus/icons-vue';
  
    export default{
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
    };
  </script>
  <style module>
    .homeChild {
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
    .maskGroupIcon {
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
    .homeItem {
      position: absolute;
      top: 3853.5px;
      left: -0.5px;
      border-top: 1px solid var(--color-lavender);
      box-sizing: border-box;
      width: 1441px;
      height: 1px;
    }
    .frequentlyAskedQuestions {
      position: absolute;
      top: calc(50% - 143.5px);
      left: calc(50% - 573.5px);
      font-size: var(--font-size-41xl);
      line-height: 120%;
      display: inline-block;
      width: 454px;
    }
    .question1Child {
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
    .firstQuestion {
      position: absolute;
      top: calc(50% - 44.5px);
      left: calc(50% - 318px);
      line-height: 120%;
    }
    .frameIcon {
      position: absolute;
      top: 23px;
      left: 655px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .question1 {
      position: absolute;
      top: 0px;
      left: 451px;
      width: 696px;
      height: 137px;
    }
    .groupChild {
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
    .secondQuestion {
      position: absolute;
      top: calc(50% - 11px);
      left: calc(50% - 318px);
      line-height: 120%;
    }
    .rectangleParent {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 696px;
      height: 70px;
    }
    .question2 {
      position: absolute;
      top: 153px;
      left: 451px;
      width: 696px;
      height: 70px;
    }
    .question3 {
      position: absolute;
      top: 239px;
      left: 451px;
      width: 696px;
      height: 70px;
    }
    .question4 {
      position: absolute;
      top: 325px;
      left: 451px;
      width: 696px;
      height: 70px;
    }
    .question5 {
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
    .letsGetIn {
      position: absolute;
      top: calc(50% - 360px);
      left: calc(50% - 252px);
      font-size: var(--font-size-41xl);
      line-height: 120%;
      font-family: var(--font-raleway);
      text-align: center;
    }
    .groupItem {
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
    .groupInner {
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
    .rectangleDiv {
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
    .fullName {
      position: absolute;
      top: 313px;
      left: 32px;
      font-size: var(--font-size-xl);
      line-height: 150%;
      color: var(--color-lightslategray);
    }
    .writeYourMessage {
      position: absolute;
      top: 431px;
      left: 32px;
      font-size: var(--font-size-xl);
      line-height: 150%;
      color: var(--color-lightslategray);
    }
    .getInTouch {
      position: absolute;
      top: 19px;
      left: 301px;
      line-height: 150%;
    }
    .getInTouchWrapper {
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
    .letsGetInTouchParent {
      position: absolute;
      top: calc(50% - 360px);
      left: calc(50% - 348px);
      width: 696px;
      height: 720px;
    }
    .letsGetInTouch {
      position: absolute;
      top: calc(50% + 1292.5px);
      left: calc(50% - 348px);
      width: 696px;
      height: 720px;
      font-family: var(--paragraph);
    }
    .yourDigital {
      margin: 0;
    }
    .yourDigitalLegalContainer {
      position: absolute;
      top: calc(50% - 157.5px);
      left: calc(50% - 504.5px);
      line-height: 100%;
      display: inline-block;
      width: 1009px;
      height: 229px;
    }
    .rectangleButton {
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
    .getStarted {
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
    .rectangleGroup {
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
    .signIn {
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
    .signUpChild {
      position: absolute;
      top: 0px;
      left: 0px;
      border-radius: var(--br-3xs);
      background-color: var(--color-darkslategray);
      width: 132px;
      height: 48px;
    }
    .signUp1 {
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
    .signUp {
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
    .signInSignUp {
      position: absolute;
      top: 26px;
      left: 1127px;
      width: 201px;
      height: 48px;
    }
    .checkOurWorkPic {
      position: absolute;
      top: -87px;
      left: calc(50% - 399.5px);
      width: 799px;
      height: 841px;
      object-fit: cover;
      display: none;
      mix-blend-mode: color-burn;
    }
    .checkOurWork1 {
      position: absolute;
      top: calc(50% - 36px);
      left: calc(50% - 227.5px);
      line-height: 120%;
    }
    .checkOurWork {
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
    .pricingSlogon {
      position: absolute;
      top: calc(50% - 221.5px);
      left: calc(50% - 521.5px);
      width: 282px;
      height: 109px;
    }
    .groupChild1 {
      position: absolute;
      top: 0px;
      left: 0px;
      border-radius: var(--br-xl);
      background-color: #4e47ff;
      width: 624px;
      height: 497px;
      mix-blend-mode: linear-dodge;
    }
    .groupChild2 {
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
    .frameIcon5 {
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
    .groupParent {
      position: absolute;
      top: 193px;
      left: 50px;
      width: 50px;
      height: 111px;
    }
    .groupDiv {
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
    .groupContainer {
      position: absolute;
      top: 193px;
      left: 331px;
      width: 46px;
      height: 111px;
    }
    .frameIcon11 {
      position: absolute;
      top: 400px;
      left: 531px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .rectangleContainer {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 624px;
      height: 497px;
    }
    .pricingBlock {
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
    .topBarChild {
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
    .howItWorks {
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
    .topBar {
      position: absolute;
      top: 16px;
      left: 471px;
      width: 499px;
      height: 68px;
    }
    .whatWeDo1 {
      position: absolute;
      top: calc(50% - 178px);
      left: calc(50% - 608px);
      font-size: var(--font-size-41xl);
      line-height: 120%;
      font-family: var(--font-raleway);
    }
    .whatWeDoBlock1Child {
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
    .whatWeDoBlock1Item {
      position: absolute;
      top: 29px;
      left: 26px;
      border-radius: var(--br-4xs);
      background-color: var(--color-ghostwhite);
      width: 44px;
      height: 44px;
      mix-blend-mode: normal;
    }
    .block1Icon {
      position: absolute;
      top: 39px;
      left: 36px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .whatWeDoBlock1 {
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
    .groupChild3 {
      position: absolute;
      top: 0px;
      left: 0px;
      border-radius: var(--br-4xs);
      background-color: var(--color-ghostwhite);
      width: 44px;
      height: 44px;
    }
    .whatWeDoBlock2Inner {
      position: absolute;
      top: 29px;
      left: 24px;
      width: 44px;
      height: 44px;
    }
    .frameIcon12 {
      position: absolute;
      top: 39px;
      left: 34px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .whatWeDoBlock2 {
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
    .whatWeDoBlock3Inner {
      position: absolute;
      top: 29px;
      left: 22px;
      width: 44px;
      height: 44px;
    }
    .frameIcon13 {
      position: absolute;
      top: 40px;
      left: 32px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .whatWeDoBlock3 {
      position: absolute;
      top: 104px;
      left: 624px;
      width: 280px;
      height: 252px;
    }
    .whatWeDoBlock4Child {
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
    .whatWeDoBlock4Inner {
      position: absolute;
      top: 29px;
      left: 29px;
      width: 44px;
      height: 44px;
    }
    .frameIcon14 {
      position: absolute;
      top: 39px;
      left: 39px;
      width: 24px;
      height: 24px;
      overflow: hidden;
    }
    .whatWeDoBlock4 {
      position: absolute;
      top: 104px;
      left: 927px;
      width: 289px;
      height: 252px;
    }
    .whatWeDo {
      position: absolute;
      top: calc(50% - 2027.5px);
      left: calc(50% - 608px);
      width: 1216px;
      height: 356px;
      font-size: var(--font-size-lgi-8);
      font-family: var(--paragraph);
    }
    .themisAi {
      position: absolute;
      top: 28px;
      left: 39px;
      line-height: 150%;
      display: inline-block;
      width: 197px;
      height: 29px;
    }
    .logo1Icon {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 81px;
      height: 88px;
      object-fit: cover;
    }
    .logoTop {
      position: absolute;
      top: 11px;
      left: 77px;
      width: 236px;
      height: 88px;
      text-align: center;
      font-size: var(--font-size-xl);
      color: var(--color-black);
    }
    .bottomContactInformationChild {
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
    .basicInfo {
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
    .howItWorks1 {
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
    .homeParent {
      position: absolute;
      top: 155px;
      left: 743px;
      width: 401px;
      height: 24px;
    }
    .themisAi1 {
      position: absolute;
      top: 36px;
      left: 63.6px;
      line-height: 150%;
      display: inline-block;
      width: 255.4px;
      height: 37.2px;
    }
    .logo1Icon1 {
      position: absolute;
      top: 0px;
      left: 0px;
      width: 105px;
      height: 113px;
      object-fit: cover;
    }
    .logoBottom {
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
    .bottomContactInformation {
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
    .firstWrapper {
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
    .frameParent {
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
  
