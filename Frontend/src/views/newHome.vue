<template>
  <div class="home">
    <img class="slogan-pic-icon" alt="" src="@/assets/slogan-pic.png" />
    <div class="slogan">
      <b class="your-digital-legal-container">
        <p class="your-digital">Your Digital</p>
        <p class="your-digital">Legal Assistant</p>
        <p class="your-digital">Always Ready</p>
      </b>
    </div>
    <div class="check-our-work">
      <div class="check-our-work-child" />
      <b class="check-our-work1">Check our Work</b>
    </div>
    <img class="check-our-work-pic" alt="" src="@/assets/checkOurWorkPic.png" />
    <div class="what-we-do">
      <b class="what-we-do1">What We do</b>
    </div>
    <div class="logo-top1">
      <b class="themis-ai1">THEMIS AI</b>
      <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
    </div>
    <div class="lets-get-in-touch">
      <div class="lets-get-in-touch-child" />
      <b class="lets-get-in">Let’s Get in Touch</b>
      <div class="lets-get-in-touch-item" />
      <b class="email">email</b>
      <div class="lets-get-in-touch-inner" />
      <div class="rectangle-div" />
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
    <div class="doc-review">
      <div class="doc-review-child" />
      <div class="doc-review1">Doc Review</div>
      <div class="rapidly-identify-critical">
        Rapidly identify critical information and potential risks within
        documents to safeguard your legal processes
      </div>
      <img class="medical-icons" alt="" src="@/assets/Docreview.png" />
    </div>
    <div class="deposition-prep">
      <div class="doc-review-child" />
      <div class="doc-review1">Deposition Prep</div>
      <div class="craft-precise-deposition">
        Craft precise deposition questions and simulate the deposition
        environment to enhance your preparedness
      </div>
      <img class="medical-icons1" alt="" src="@/assets/DepositionPrep.png" />
    </div>
    <div class="legal-research">
      <div class="doc-review-child" />
      <div class="doc-review1">Legal Research</div>
      <div class="expedite-the-retrieval">
        Expedite the retrieval and analysis of legal information to support your
        decision-making processes
      </div>
      <img class="medical-icons2" alt="" src="@/assets/LegalResearch.png" />
    </div>
    <div class="personalized-writing-style">
      <div class="doc-review-child" />
      <div class="personalized-writing-style1">Personalized Writing Style</div>
      <div class="ensure-the-ai-generated">
        Ensure the AI-generated content matches the unique writing style of the
        lawyer, saving significant time and effort in revisions.
      </div>
      <img class="medical-icons3" alt="" src="@/assets/PersonalizedWritingStyle.png" />
    </div>
    <div class="local-regulations">
      <div class="doc-review-child" />
      <div class="doc-review1">Local Regulations</div>
      <div class="provide-summaries-of">
        Provide summaries of local regulations tailored to specific
        jurisdictions to ensure your compliance and strategic alignment
      </div>
      <img class="medical-icons4" alt="" src="@/assets/LocalRegulations.png" />
    </div>
    <div class="paralegal-training">
      <div class="doc-review-child" />
      <div class="doc-review1">Paralegal Training</div>
      <div class="expedite-the-retrieval">
        Streamline the onboarding process for new hires by providing new
        employees with immediate
      </div>
      <img class="medical-icons5" alt="" src="@/assets/ParalegalTraining.png" />
    </div>
    <div class="case-analysis">
      <img class="case-analysis-child" />
      <div class="doc-review1">Case Analysis</div>
      <div class="craft-precise-deposition">
        Assists in dissecting legal precedents and relevant laws to bolster your
        case strategies
      </div>
      <img class="medical-icons6" alt="" src="@/assets/CaseAnalysis.png" />
    </div>
    <div class="auto-fill">
      <div class="doc-review-child" />
      <div class="doc-review1">Auto Fill</div>
      <div class="automates-the-filling">
        Automates the filling of repetitive information across multiple
        documents to ensure the accuracy and uniformity
      </div>
      <img class="medical-icons7" alt="" src="@/assets/AutoFill.png" />
    </div>
    <div class="home-page-get-started">
      <button class="get-started1" :autoFocus="true" @click="onGetStartedClick">
        Get Started
      </button>
    </div>
    <div class="top-bar">
      <div class="home-page-service">
        <button class="about" :autoFocus="true">About</button>
      </div>
      <div class="home-page-service1">
        <button class="about" :autoFocus="true">Service</button>
      </div>
      <div class="home-page-service">
        <button class="about" :autoFocus="true">Price</button>
      </div>
      <div class="home-page-service3">
        <button class="about" :autoFocus="true">FAQs</button>
      </div>
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
    <div class="questions">
      <b class="why-themis-ai">Why Themis AI</b>
    </div>
    <div class="logo-top2">
      <b class="themis-ai1">THEMIS AI</b>
      <img class="logo-1-icon1" alt="" src="@/assets/logo.png" />
    </div>
    <div class="linkedin">Linkedin</div>
    <div class="schedule-demo" @click="onScheduleDemoTextClick">
      Schedule Demo
    </div>
    <div class="pricing" @click="onPricingTextClick">Pricing</div>
    <div class="contact-us" @click="onScheduleDemoTextClick">Contact Us</div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "Home",
    methods: {
      onGetStartedClick() {
        this.$router.push("/");
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
  .your-digital {
    margin: 0;
  }
  .your-digital-legal-container {
    position: absolute;
    top: calc(50% - 114.5px);
    left: calc(50% - 504.5px);
    line-height: 100%;
    display: inline-block;
    width: 1009px;
    height: 229px;
  }
  .slogan {
    position: absolute;
    top: calc(50% - 2469.5px);
    left: calc(50% - 504px);
    width: 1009px;
    height: 229px;
    text-align: center;
    font-size: 73.3px;
    font-family: var(--font-raleway);
  }
  .check-our-work-child {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: var(--color-white);
    width: 1440px;
    height: 961px;
  }
  .check-our-work1 {
    position: absolute;
    top: calc(50% - 366.5px);
    left: calc(50% - 227px);
    line-height: 120%;
  }
  .check-our-work {
    position: absolute;
    top: 2249px;
    left: 0px;
    width: 1440px;
    height: 961px;
    font-size: var(--font-size-41xl);
    color: #011427;
    font-family: var(--font-raleway);
  }
  .check-our-work-pic {
    position: absolute;
    top: 2476px;
    left: -794px;
    width: 2122px;
    height: 1269px;
    object-fit: contain;
    opacity: 0.5;
  }
  .what-we-do1 {
    position: absolute;
    top: calc(50% - 36px);
    left: calc(50% - 177px);
    line-height: 120%;
  }
  .what-we-do {
    position: absolute;
    top: calc(50% - 1980.5px);
    left: calc(50% - 588px);
    width: 354px;
    height: 72px;
    font-size: var(--font-size-41xl);
    font-family: var(--font-raleway);
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
    font-family: var(--font-saira);
  }
  .lets-get-in-touch-child {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: var(--color-white);
    width: 1440px;
    height: 915px;
  }
  .lets-get-in {
    position: absolute;
    top: calc(50% - 359.5px);
    left: calc(50% - 251px);
    font-size: var(--font-size-41xl);
    line-height: 120%;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .lets-get-in-touch-item {
    position: absolute;
    top: 225px;
    left: 371px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .email {
    position: absolute;
    top: calc(50% - 264.5px);
    left: calc(50% - 342px);
    line-height: 120%;
  }
  .lets-get-in-touch-inner {
    position: absolute;
    top: 343px;
    left: 371px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 70px;
    mix-blend-mode: normal;
  }
  .rectangle-div {
    position: absolute;
    top: 461px;
    left: 371px;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    width: 696px;
    height: 222px;
    mix-blend-mode: normal;
  }
  .name {
    position: absolute;
    top: calc(50% - 144.5px);
    left: calc(50% - 342px);
    line-height: 120%;
  }
  .message {
    position: absolute;
    top: calc(50% - 26.5px);
    left: calc(50% - 342px);
    line-height: 120%;
  }
  .exampleemailcom {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 245px;
    left: 403px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .full-name {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 363px;
    left: 403px;
    line-height: 150%;
    color: var(--color-lightslategray-200);
    text-align: left;
  }
  .write-your-message {
    border: none;
    outline: none;
    font-family: var(--font-inter);
    font-size: var(--font-size-xl);
    background-color: transparent;
    position: absolute;
    top: 481px;
    left: 403px;
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
    height: 7.37%;
    width: 48.33%;
    top: 82.24%;
    right: 25.9%;
    bottom: 10.39%;
    left: 25.76%;
    border-radius: var(--br-3xs);
    overflow: hidden;
  }
  .lets-get-in-touch {
    position: absolute;
    top: 4099px;
    left: -1px;
    width: 1440px;
    height: 915px;
    font-size: var(--font-size-lg);
    color: var(--color-gray-300);
  }
  .doc-review-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-gray-400);
    width: 632px;
    height: 287px;
    mix-blend-mode: linear-dodge;
  }
  .doc-review1 {
    position: absolute;
    top: calc(50% - 91.5px);
    left: calc(50% - 152px);
    line-height: 120%;
    font-weight: 600;
  }
  .rapidly-identify-critical {
    position: absolute;
    top: 134px;
    left: 39px;
    font-size: var(--font-size-11xl);
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 591px;
  }
  .medical-icons {
    position: absolute;
    top: 31px;
    left: 39px;
    width: 84px;
    height: 98px;
    overflow: hidden;
  }
  .doc-review {
    position: absolute;
    top: 815px;
    left: 74px;
    width: 632px;
    height: 287px;
  }
  .craft-precise-deposition {
    position: absolute;
    top: 133px;
    left: 30px;
    font-size: var(--font-size-11xl);
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 591px;
  }
  .medical-icons1 {
    position: absolute;
    top: 38px;
    left: 32px;
    width: 90px;
    height: 66.4px;
    overflow: hidden;
  }
  .deposition-prep {
    position: absolute;
    top: 1133px;
    left: 74px;
    width: 632px;
    height: 287px;
  }
  .expedite-the-retrieval {
    position: absolute;
    top: 133px;
    left: 30px;
    font-size: var(--font-size-11xl);
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 581px;
  }
  .medical-icons2 {
    position: absolute;
    top: 37px;
    left: 41px;
    width: 90px;
    height: 82.6px;
    overflow: hidden;
  }
  .legal-research {
    position: absolute;
    top: 1443px;
    left: 74px;
    width: 632px;
    height: 287px;
  }
  .personalized-writing-style1 {
    position: absolute;
    top: calc(50% - 91.5px);
    left: calc(50% - 161px);
    line-height: 120%;
    font-weight: 600;
  }
  .ensure-the-ai-generated {
    position: absolute;
    top: 133px;
    left: 30px;
    font-size: 27px;
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 581px;
  }
  .medical-icons3 {
    position: absolute;
    top: 18px;
    left: 43px;
    width: 75px;
    height: 94.6px;
    overflow: hidden;
  }
  .personalized-writing-style {
    position: absolute;
    top: 1753px;
    left: 74px;
    width: 632px;
    height: 287px;
    font-size: 36px;
  }
  .provide-summaries-of {
    position: absolute;
    top: 133px;
    left: 30px;
    font-size: 28px;
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 581px;
  }
  .medical-icons4 {
    position: absolute;
    top: 46px;
    left: 32px;
    width: 100px;
    height: 54.2px;
    overflow: hidden;
  }
  .local-regulations {
    position: absolute;
    top: 1443px;
    left: 738px;
    width: 632px;
    height: 287px;
  }
  .medical-icons5 {
    position: absolute;
    top: 32px;
    left: 36px;
    width: 110px;
    height: 77.5px;
    overflow: hidden;
  }
  .paralegal-training {
    position: absolute;
    top: 1753px;
    left: 738px;
    width: 632px;
    height: 287px;
  }
  .case-analysis-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    width: 632px;
    height: 287px;
    mix-blend-mode: linear-dodge;
  }
  .medical-icons6 {
    position: absolute;
    top: 42px;
    left: 32px;
    width: 100px;
    height: 62.4px;
    overflow: hidden;
  }
  .case-analysis {
    position: absolute;
    top: 1133px;
    left: 736px;
    width: 632px;
    height: 287px;
  }
  .automates-the-filling {
    position: absolute;
    top: 134px;
    left: 43px;
    font-size: var(--font-size-11xl);
    line-height: 150%;
    color: var(--color-silver);
    display: inline-block;
    width: 571px;
  }
  .medical-icons7 {
    position: absolute;
    top: 35px;
    left: 43px;
    width: 88px;
    height: 90.2px;
    overflow: hidden;
  }
  .auto-fill {
    position: absolute;
    top: 815px;
    left: 736px;
    width: 632px;
    height: 287px;
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
    top: 505px;
    left: calc(50% - 116.5px);
    border-radius: var(--br-3xs);
    background-color: var(--color-white);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-lg) var(--padding-42xl);
  }
  .about {
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
  .why-themis-ai {
    position: absolute;
    top: calc(50% - 36px);
    left: calc(50% - 214px);
    line-height: 120%;
    display: inline-block;
    width: 428px;
  }
  .questions {
    position: absolute;
    top: calc(50% + 615.5px);
    left: calc(50% - 217px);
    width: 428px;
    height: 72px;
    font-size: var(--font-size-41xl);
    font-family: var(--font-raleway);
  }
  .logo-top2 {
    position: absolute;
    top: 5068px;
    left: 77px;
    width: 236px;
    height: 88px;
    text-align: center;
    font-size: var(--font-size-xl);
    font-family: var(--font-saira);
  }
  .linkedin {
    position: absolute;
    top: 5096px;
    left: 406px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 500;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .schedule-demo {
    position: absolute;
    top: 5096px;
    left: 561px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 500;
    font-family: var(--font-raleway);
    text-align: center;
    cursor: pointer;
  }
  .pricing {
    position: absolute;
    top: 5096px;
    left: 786px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 500;
    font-family: var(--font-raleway);
    text-align: center;
    cursor: pointer;
  }
  .contact-us {
    position: absolute;
    top: 5097px;
    left: 926px;
    font-size: var(--font-size-xl);
    line-height: 150%;
    font-weight: 500;
    font-family: var(--font-raleway);
    text-align: center;
    cursor: pointer;
  }
  .home {
    width: 100%;
    position: relative;
    background: linear-gradient(
        90.08deg,
        rgba(250, 255, 4, 0),
        rgba(250, 255, 4, 0.2)
      ),
      #001326;
    height: 5371px;
    text-align: left;
    font-size: var(--font-size-21xl);
    color: var(--color-white);
    font-family: var(--font-inter);
  }
</style>
