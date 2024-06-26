<template>
  <div class="contact-us3">
    <img class="slogan-pic-icon2" alt="" src="@/assets/slogan-pic.png" />
    <div class="top-bar2">
      <div class="home-page-service8">
        <button class="about3" :autoFocus="true">About</button>
      </div>
      <div class="home-page-service9">
        <button class="about3" :autoFocus="true">Service</button>
      </div>
      <div class="home-page-service8">
        <button class="about3" :autoFocus="true">Price</button>
      </div>
      <div class="home-page-service11">
        <button class="about3" :autoFocus="true">FAQs</button>
      </div>
    </div>
    <div class="logo-top5" @click="onLogoTopContainerClick">
      <b class="themis-ai5">THEMIS AI</b>
      <img class="logo-1-icon5" alt="" src="@/assets/logo.png" />
    </div>
    <div class="logo-top6" @click="onLogoTopContainerClick">
      <b class="themis-ai5">THEMIS AI</b>
      <img class="logo-1-icon5" alt="" src="@/assets/logo.png" />
    </div>
    <div class="home-page-sign-in2">
      <button class="sign-in2" :autoFocus="true" @click="onSignInClick">
        Sign In
      </button>
    </div>
    <button class="home-page-sign-up2" :autoFocus="true">
      <button class="sign-up3" :autoFocus="true" @click="onSignUpClick">
        Sign Up
      </button>
    </button>
    <div class="contact-us-child" />
    <div class="linkedin2">Linkedin</div>
    <div class="schedule-demo2">Schedule Demo</div>
    <div class="pricing3">Pricing</div>
    <div class="contact-us4">Contact Us</div>
    <b class="contact-themis-ai">Contact Themis AI</b>
    <b class="lets-get-in">Let’s Get in Touch</b>
    <div class="contact-us-item" />
    <b class="email">Email</b>
    <div class="contact-us-inner" />
    <div class="rectangle-div" />
    <b class="full-name">Full Name</b>
    <b class="message">Message</b>
    <input
      class="exampleemailcom"
      placeholder="example@email.com"
      type="text"
    />
    <div class="contact-us-child1" />
    <b class="your-job-title">Your Job Title</b>
    <input class="eg-paralegal" placeholder="E.g. paralegal" type="text" />
    <input class="full-name1" placeholder="full name" type="text" />
    <input
      class="request-demo-write"
      placeholder="request demo/ write your message...."
      type="text"
    />
    <button class="get-in-touch-wrapper">
      <b class="get-in-touch">Get in Touch</b>
    </button>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "ContactUs",
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
    },
  });
</script>
<style scoped>
  .slogan-pic-icon2 {
    position: absolute;
    top: -91px;
    left: 241px;
    width: 945px;
    height: 945px;
  }
  .about3 {
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
  .home-page-service8 {
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
  .home-page-service9 {
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
  .home-page-service11 {
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
  .top-bar2 {
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
  .themis-ai5 {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
  }
  .logo-1-icon5 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
  }
  .logo-top5 {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .logo-top6 {
    position: absolute;
    top: 1256px;
    left: 77px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .sign-in2 {
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
  .home-page-sign-in2 {
    position: absolute;
    top: 38px;
    left: 1119px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .sign-up3 {
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
  .home-page-sign-up2 {
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
  .contact-us-child {
    position: absolute;
    top: 300px;
    left: calc(50% - 441px);
    border-radius: var(--br-xl);
    background-color: var(--color-white);
    width: 882px;
    height: 894px;
  }
  .linkedin2 {
    position: absolute;
    top: 1284px;
    left: 406px;
    line-height: 150%;
    font-weight: 500;
  }
  .schedule-demo2 {
    position: absolute;
    top: 1284px;
    left: 559px;
    line-height: 150%;
    font-weight: 500;
  }
  .pricing3 {
    position: absolute;
    top: 1284px;
    left: 784px;
    line-height: 150%;
    font-weight: 500;
  }
  .contact-us4 {
    position: absolute;
    top: 1285px;
    left: 924px;
    line-height: 150%;
    font-weight: 500;
  }
  .contact-themis-ai {
    position: absolute;
    top: 156px;
    left: calc(50% - 217px);
    font-size: var(--font-size-31xl);
    line-height: 150%;
  }
  .lets-get-in {
    position: absolute;
    top: calc(50% - 715px);
    left: calc(50% - 167px);
    font-size: var(--font-size-21xl);
    line-height: 120%;
    color: var(--color-gray-300);
  }
  .contact-us-item {
    position: absolute;
    top: 595px;
    left: calc(50% - 348px);
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .email {
    position: absolute;
    top: calc(50% - 508px);
    left: calc(50% - 341px);
    font-size: var(--font-size-lg);
    line-height: 120%;
    font-family: var(--font-inter);
    color: var(--color-gray-300);
    text-align: left;
  }
  .contact-us-inner {
    position: absolute;
    top: 485px;
    left: 372px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .rectangle-div {
    position: absolute;
    top: 816px;
    left: 372px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 222px;
    mix-blend-mode: normal;
  }
  .full-name {
    position: absolute;
    top: calc(50% - 617px);
    left: calc(50% - 341px);
    font-size: var(--font-size-lg);
    line-height: 120%;
    font-family: var(--font-inter);
    color: var(--color-gray-300);
    text-align: left;
  }
  .message {
    position: absolute;
    top: calc(50% - 286px);
    left: calc(50% - 341px);
    font-size: var(--font-size-lg);
    line-height: 120%;
    font-family: var(--font-inter);
    color: var(--color-gray-300);
    text-align: left;
  }
  .exampleemailcom {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 615px;
    left: 401px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .contact-us-child1 {
    position: absolute;
    top: 705px;
    left: calc(50% - 348px);
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .your-job-title {
    position: absolute;
    top: calc(50% - 398px);
    left: calc(50% - 341px);
    font-size: var(--font-size-lg);
    line-height: 120%;
    font-family: var(--font-inter);
    color: var(--color-gray-300);
    text-align: left;
  }
  .eg-paralegal {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 725px;
    left: 401px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .full-name1 {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 505px;
    left: 404px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .request-demo-write {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 836px;
    left: 404px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .get-in-touch {
    position: absolute;
    top: 19px;
    left: 301px;
    font-size: var(--font-size-base);
    line-height: 150%;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
  }
  .get-in-touch-wrapper {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: var(--color-gray-300);
    position: absolute;
    height: 3.14%;
    top: 51.21%;
    bottom: 45.64%;
    left: calc(50% - 348px);
    border-radius: var(--br-3xs);
    width: 696px;
    overflow: hidden;
  }
  .contact-us3 {
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
