<template>
  <div class="pricing1">
    <img class="slogan-pic-icon1" alt="" src="@/assets/slogan-pic.png" />
    <div class="top-bar1">
      <div class="home-page-service4">
        <button class="about2" :autoFocus="true">About</button>
      </div>
      <div class="home-page-service5">
        <button class="about2" :autoFocus="true">Service</button>
      </div>
      <div class="home-page-service4">
        <button class="about2" :autoFocus="true">Price</button>
      </div>
      <div class="home-page-service7">
        <button class="about2" :autoFocus="true">FAQs</button>
      </div>
    </div>
    <div class="logo-top3" @click="onLogoTopContainerClick">
      <b class="themis-ai3">THEMIS AI</b>
      <img class="logo-1-icon3" alt="" src="@/assets/logo.png" />
    </div>
    <div class="logo-top4" @click="onLogoTopContainerClick">
      <b class="themis-ai3">THEMIS AI</b>
      <img class="logo-1-icon3" alt="" src="@/assets/logo.png" />
    </div>
    <div class="home-page-sign-in1">
      <button class="sign-in1" :autoFocus="true" @click="onSignInClick">
        Sign In
      </button>
    </div>
    <button class="home-page-sign-up1" :autoFocus="true">
      <button class="sign-up2" :autoFocus="true" @click="onSignUpClick">
        Sign Up
      </button>
    </button>
    <div class="linkedin1">Linkedin</div>
    <div class="schedule-demo1" @click="onScheduleDemoTextClick">
      Schedule Demo
    </div>
    <div class="pricing2">Pricing</div>
    <div class="contact-us2" @click="onScheduleDemoTextClick">Contact Us</div>
    <div class="hero-pricing">
      <div class="title">
        <div class="div">
          <div class="compare-plans-wrapper">
            <b class="compare-plans">Compare plans</b>
          </div>
          <div class="choose-your-workspace">
            Choose your workspace plan according to your organisational plan
          </div>
        </div>
        <div class="div1">
          <div class="doc-review">Doc Review</div>
        </div>
        <div class="div1">
          <div class="doc-review">Auto Fill</div>
        </div>
        <div class="div1">
          <div class="doc-review">Deposition Prep</div>
        </div>
        <div class="div1">
          <div class="doc-review">Case Analysis</div>
        </div>
        <div class="div1">
          <div class="doc-review">Legal Research</div>
        </div>
        <div class="div1">
          <div class="doc-review">Local Regulations</div>
        </div>
        <div class="div1">
          <div class="doc-review">Personalized Writing Style</div>
        </div>
        <div class="div1">
          <div class="doc-review">Paralegal Training</div>
        </div>
        <div class="div1">
          <div class="doc-review">####</div>
        </div>
        <div class="div1">
          <div class="doc-review">####</div>
        </div>
        <div class="div1">
          <div class="doc-review">####</div>
        </div>
      </div>
      <div class="price-01">
        <div class="div15">
          <div class="parent">
            <b class="compare-plans">$50</b>
            <div class="month-wrapper">
              <div class="month">/Month</div>
            </div>
          </div>
          <button class="button">
            <b class="choose-this-plan">Choose This Plan</b>
          </button>
        </div>
        <div class="div16">
          <div class="month">+</div>
        </div>
        <div class="div16">
          <div class="month">+</div>
        </div>
        <div class="div20">
          <div class="month">+</div>
        </div>
        <div class="div20">
          <div class="month">+</div>
        </div>
        <div class="div20">
          <div class="month">-</div>
        </div>
        <div class="div20">
          <div class="month">-</div>
        </div>
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
      </div>
      <div class="price-01">
        <div class="div15">
          <div class="parent">
            <b class="compare-plans">$70</b>
            <div class="month-wrapper">
              <div class="month">/Month</div>
            </div>
          </div>
          <button class="button">
            <b class="choose-this-plan">Choose This Plan</b>
          </button>
        </div>
        <div class="div16">
          <div class="month">++</div>
        </div>
        <div class="div16">
          <div class="month">++</div>
        </div>
        <div class="div20">
          <div class="month">++</div>
        </div>
        <div class="div20">
          <div class="month">++</div>
        </div>
        <div class="div20">
          <div class="month">+</div>
        </div>
        <div class="div20">
          <div class="month">-</div>
        </div>
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
      </div>
      <div class="price-01">
        <div class="div15">
          <div class="parent">
            <b class="compare-plans">$80</b>
            <div class="month-wrapper">
              <div class="month">/Month</div>
            </div>
          </div>
          <button class="button">
            <b class="choose-this-plan">Choose This Plan</b>
          </button>
        </div>
        <div class="div16">
          <div class="month">+++</div>
        </div>
        <div class="div16">
          <div class="month">+++</div>
        </div>
        <div class="div20">
          <div class="month">+++</div>
        </div>
        <div class="div20">
          <div class="month">+++</div>
        </div>
        <div class="div20">
          <div class="month">+</div>
        </div>
        <div class="div20">
          <div class="month">+</div>
        </div>
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
        <div class="div28" />
      </div>
    </div>
    <b class="find-your-perfect">Find Your Perfect Plan</b>
    <div class="discover-the-perfect">
      Discover the perfect plan to enhance your legal practice. Our pricing
      options are thoughtfully designed to meet the needs of law firms and legal
      professionals.
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Pricing",
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
      onScheduleDemoTextClick() {
        this.$router.push("/contact-us");
      },
    },
  });
</script>
<style scoped>
  .slogan-pic-icon1 {
    position: absolute;
    top: -91px;
    left: 241px;
    width: 945px;
    height: 945px;
  }
  .about2 {
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
  .home-page-service4 {
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
  .home-page-service5 {
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
  .home-page-service7 {
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
  .top-bar1 {
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
  .themis-ai3 {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
  }
  .logo-1-icon3 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
  }
  .logo-top3 {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .logo-top4 {
    position: absolute;
    top: 1619px;
    left: 77px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    font-family: var(--font-saira);
  }
  .sign-in1 {
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
  .home-page-sign-in1 {
    position: absolute;
    top: 38px;
    left: 1119px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .sign-up2 {
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
  .home-page-sign-up1 {
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
  .linkedin1 {
    position: absolute;
    top: 1647px;
    left: 406px;
    line-height: 150%;
    font-weight: 500;
  }
  .schedule-demo1 {
    position: absolute;
    top: 1647px;
    left: 559px;
    line-height: 150%;
    font-weight: 500;
    cursor: pointer;
  }
  .pricing2 {
    position: absolute;
    top: 1647px;
    left: 784px;
    line-height: 150%;
    font-weight: 500;
  }
  .contact-us2 {
    position: absolute;
    top: 1648px;
    left: 924px;
    line-height: 150%;
    font-weight: 500;
    cursor: pointer;
  }
  .compare-plans {
    position: relative;
  }
  .compare-plans-wrapper {
    align-self: stretch;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
  }
  .choose-your-workspace {
    align-self: stretch;
    position: relative;
    font-size: var(--font-size-sm);
    line-height: 20px;
    font-weight: 500;
    font-family: var(--font-inter);
    color: var(--color-lightslategray-100);
  }
  .div {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    height: 183px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    padding: var(--padding-xl) var(--padding-13xl);
    gap: var(--gap-xs);
    font-size: 24px;
    font-family: var(--font-roboto);
  }
  .doc-review {
    flex: 1;
    position: relative;
    line-height: 26px;
    font-weight: 500;
  }
  .div1 {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    height: 80px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-xl) var(--padding-13xl);
  }
  .title {
    flex: 1;
    border-right: 1px solid var(--color-lavender-100);
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    font-size: var(--font-size-lg);
    color: var(--color-gray-100);
  }
  .month {
    position: relative;
    line-height: 20px;
    font-weight: 500;
  }
  .month-wrapper {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: flex-start;
    padding: var(--padding-6xs) 0px;
    font-size: var(--font-size-sm);
    color: var(--color-lightslategray-100);
    font-family: var(--font-inter);
  }
  .parent {
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: center;
    gap: var(--gap-5xs);
  }
  .choose-this-plan {
    flex: 1;
    position: relative;
    font-size: var(--font-size-sm);
    line-height: 20px;
    font-family: var(--font-inter);
    color: var(--color-lavender-200);
    text-align: center;
  }
  .button {
    cursor: pointer;
    border: none;
    padding: var(--padding-base) var(--padding-5xl);
    background-color: var(--color-gray-100);
    align-self: stretch;
    border-radius: var(--br-9xs);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .div15 {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--padding-9xl);
    gap: var(--gap-9xl);
    font-size: var(--font-size-21xl);
    color: var(--color-gray-100);
    font-family: var(--font-roboto);
  }
  .div16 {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    height: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--padding-xl) 0px;
  }
  .div20 {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    height: 80px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-xl) var(--padding-104xl);
  }
  .div28 {
    align-self: stretch;
    border-bottom: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    height: 80px;
  }
  .price-01 {
    flex: 1;
    border-right: 1px solid var(--color-lavender-100);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .hero-pricing {
    position: absolute;
    top: 513px;
    left: calc(50% - 568px);
    border-radius: var(--br-xl);
    background-color: var(--color-white);
    border: 1px solid var(--color-lavender-100);
    box-sizing: border-box;
    width: 1136px;
    height: 1063px;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    text-align: left;
    font-size: var(--font-size-31xl);
    color: var(--color-black);
    font-family: var(--font-inter);
  }
  .find-your-perfect {
    position: absolute;
    top: 163px;
    left: calc(50% - 316px);
    font-size: var(--font-size-41xl);
    line-height: 150%;
  }
  .discover-the-perfect {
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
  .pricing1 {
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
