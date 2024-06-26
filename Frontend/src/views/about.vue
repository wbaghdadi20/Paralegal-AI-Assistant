<template>
  <div class="about">
    <img class="slogan-pic-icon" alt="" src="/slogan-pic.svg" />
    <div class="about-child" />
    <div class="top-bar">
      <div class="home-page-service">
        <button class="price" :autoFocus="true">About</button>
      </div>
      <div class="home-page-service1">
        <button class="price" :autoFocus="true">Service</button>
      </div>
      <div class="home-page-service">
        <button class="price" :autoFocus="true">Price</button>
      </div>
      <div class="home-page-service3">
        <button class="price" :autoFocus="true">FAQs</button>
      </div>
    </div>
    <img class="check-our-work-pic" alt="" src="@/assets/checkOurWorkPic.png" />
    <div class="logo-top1" @click="onLogoTopContainerClick">
      <b class="themis-ai1">THEMIS AI</b>
      <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
    </div>
    <div class="logo-top2" @click="onLogoTopContainerClick">
      <b class="themis-ai1">THEMIS AI</b>
      <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
    </div>
    <div class="home-page-sign-in">
      <button class="sign-in" :autoFocus="true" @click="onSignInClick">
        Sign In
      </button>
    </div>
    <button class="home-page-sign-up" :autoFocus="true">
      <button class="sign-up1" :autoFocus="true" @click="onSignUpClick">
        Sign Up
      </button>
    </button>
    <b class="legal-intelligence-perfected"
      >Legal Intelligence, Perfected by AI</b
    >
    <div class="empower-legal-professionals">
      Empower legal professionals to delegate substantive work to AI, ensuring
      accuracy and efficiency.
    </div>
    <div class="frame-parent">
      <div class="leaders-in-legal-ai-innovation-parent">
        <b class="leaders-in-legal">Leaders in Legal AI Innovation</b>
        <div class="themis-ai-led">
          THEMIS AI led innovation in legal technology by leveraging advanced AI
          and machine learning to build sophisticated tools for legal
          professionals.
        </div>
      </div>
      <div class="ai-designed-for-legal-professi-parent">
        <b class="leaders-in-legal">AI Designed for Legal Professionals</b>
        <div class="themis-ai-led">
          THEMIS AI are designed to work seamlessly within existing workflows,
          ensuring that the latest technology is utilized to its fullest
          potential.
        </div>
      </div>
      <div class="ai-designed-for-legal-professi-parent">
        <b class="leaders-in-legal">Committed to Technological Excellence</b>
        <div class="themis-ai-led">
          THEMIS AI are committed to continuously testing and refining our
          technology to guarantee the legal profession's progress.
        </div>
      </div>
    </div>
    <div class="home-page-get-started">
      <button class="get-started1" :autoFocus="true" @click="onGetStartedClick">
        Get Started
      </button>
    </div>
    <div class="contact-us-parent">
      <b class="leaders-in-legal">Contact Us:</b>
      <b class="leaders-in-legal">example@email</b>
    </div>
    <div class="linkedin">Linkedin</div>
    <div class="schedule-demo" @click="onScheduleDemoTextClick">
      Schedule Demo
    </div>
    <div class="pricing" @click="onPricingTextClick">Pricing</div>
    <div class="contact-us1" @click="onScheduleDemoTextClick">Contact Us</div>
    <img class="about-item" alt="" src="@/assets/Vector1.png" />
    <img class="about-inner" alt="" src="@/assets/Vector1.png" />
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "About",
    methods: {
      onLogoTopContainerClick() {
        this.$router.push("/home");
      },
      onSignInClick() {
        this.$router.push("/sign-in");
      },
      onSignUpClick() {
        this.$router.push("/sign-up");
      },
      onGetStartedClick() {
        this.$router.push("/");
      },
      onScheduleDemoTextClick() {
        this.$router.push("/contact-us");
      },
      onPricingTextClick() {
        this.$router.push("/pricing");
      },
    },
  });
</script>
<style scoped>
  .slogan-pic-icon {
    position: absolute;
    top: -91px;
    left: 241px;
    width: 945px;
    height: 945px;
  }
  .about-child {
    position: absolute;
    top: 451px;
    left: 0px;
    background-color: var(--color-white);
    width: 1440px;
    height: 1081px;
  }
  .home-page-service {
    width: 92px;
    border-radius: var(--br-3xs);
    height: 34px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .home-page-service1 {
    width: 92px;
    border-radius: var(--br-3xs);
    height: 40px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .price {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 600;
    font-family: var(--font-raleway);
    color: var(--color-black);
    text-align: left;
    display: inline-block;
  }
  .home-page-service3 {
    width: 63px;
    border-radius: var(--br-3xs);
    height: 40px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .top-bar {
    position: absolute;
    top: 22px;
    left: calc(50% - 259px);
    border-radius: var(--br-3xs);
    background-color: var(--color-gray-500);
    width: 518px;
    height: 53px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xl) var(--padding-35xl);
    box-sizing: border-box;
    gap: var(--gap-xl);
  }
  .check-our-work-pic {
    position: absolute;
    top: 920px;
    left: 387px;
    width: 1798px;
    height: 1069px;
    opacity: 0.5;
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
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .logo-top2 {
    position: absolute;
    top: 1587px;
    left: 77px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .sign-in {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-base);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: left;
    display: inline-block;
  }
  .home-page-sign-in {
    position: absolute;
    top: 38px;
    left: 1119px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .sign-up1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-base);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-darkslategray-200);
    text-align: center;
    display: inline-block;
  }
  .home-page-sign-up {
    cursor: pointer;
    border: none;
    padding: var(--padding-xs) var(--padding-17xl);
    background-color: var(--color-white);
    position: absolute;
    top: 26px;
    left: 1199px;
    border-radius: var(--br-3xs);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .legal-intelligence-perfected {
    position: absolute;
    top: 163px;
    left: 227px;
    font-size: var(--font-size-41xl);
    line-height: 150%;
  }
  .empower-legal-professionals {
    position: absolute;
    top: 251px;
    left: calc(50% - 561px);
    font-size: var(--font-size-21xl);
    line-height: 150%;
    font-weight: 600;
    color: var(--color-lightgray);
    display: inline-block;
    width: 1123px;
  }
  .leaders-in-legal {
    position: relative;
    line-height: 150%;
  }
  .themis-ai-led {
    width: 877px;
    position: relative;
    font-size: var(--font-size-6xl);
    line-height: 150%;
    font-weight: 600;
    color: var(--color-darkslategray-100);
    text-align: center;
    display: inline-block;
  }
  .leaders-in-legal-ai-innovation-parent {
    width: 955px;
    border-radius: var(--br-xl);
    height: 174px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--padding-11xl) var(--padding-3xs);
    box-sizing: border-box;
    gap: var(--gap-xl);
  }
  .ai-designed-for-legal-professi-parent {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--padding-11xl) var(--padding-3xs);
    gap: var(--gap-xl);
  }
  .frame-parent {
    position: absolute;
    top: 510px;
    left: 243px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: 40px;
    text-align: left;
    font-size: var(--font-size-16xl);
    color: var(--color-black);
  }
  .get-started1 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: relative;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-darkslategray-200);
    text-align: center;
    display: inline-block;
  }
  .home-page-get-started {
    position: absolute;
    top: 1372px;
    left: calc(50% - 117px);
    border-radius: var(--br-3xs);
    background-color: var(--color-white);
    border: 2px solid #01142a;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-lg) var(--padding-42xl);
  }
  .contact-us-parent {
    position: absolute;
    top: 1204px;
    left: 585px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    font-size: var(--font-size-16xl);
    color: var(--color-black);
  }
  .linkedin {
    position: absolute;
    top: 1615px;
    left: 406px;
    line-height: 150%;
    font-weight: 500;
  }
  .schedule-demo {
    position: absolute;
    top: 1615px;
    left: 559px;
    line-height: 150%;
    font-weight: 500;
    cursor: pointer;
  }
  .pricing {
    position: absolute;
    top: 1615px;
    left: 784px;
    line-height: 150%;
    font-weight: 500;
    cursor: pointer;
  }
  .contact-us1 {
    position: absolute;
    top: 1616px;
    left: 924px;
    line-height: 150%;
    font-weight: 500;
    cursor: pointer;
  }
  .about-item {
    position: absolute;
    top: 712px;
    left: calc(50% - 543px);
    max-height: 100%;
    width: 1086.5px;
  }
  .about-inner {
    position: absolute;
    top: 957px;
    left: calc(50% - 543px);
    max-height: 100%;
    width: 1086.5px;
  }
  .about {
    width: 100%;
    position: relative;
    background: linear-gradient(90.12deg, #001429, #31421f);
    height: 2144px;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-xl);
    color: var(--color-white);
    font-family: var(--font-raleway);
  }
</style>
