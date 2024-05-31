<template>
  <div class="sign-up2">
    <div class="logonobackground">
      <b class="themis-ai4" @click="onTHEMISAITextClick">THEMIS AI</b>
      <img
        class="logonobackground-1-icon"
        alt=""
        src="@/assets/logoNoBackground.png"
      />
    </div>
    <div class="sign-up-child" />
    <div class="sign-in-google-fb1">
      <div class="or1">OR</div>
      <div class="sign-in-options1">
        <div class="btn-google1">
          <img class="google-icon1" alt="" src="@/assets/Google.png" />
          <div class="sign-in-with2">Sign in with Google</div>
        </div>
        <div class="btn-google1">
          <img class="facebook-icon1" alt="" src="@/assets/Facebook.png" />
          <div class="sign-in-with2">Sign in with Facebook</div>
        </div>
      </div>
    </div>
    <div class="sign-up3">
      <b class="sign-up4">Sign Up</b>
      <div class="first-name">
        <b class="first-name1">First Name</b>
        <div class="first-name-child" />
        <input class="first-name2" placeholder="First Name" type="text" />
      </div>
      <div class="first-name">
        <b class="first-name1">Last Name</b>
        <div class="first-name-child" />
        <input class="last-name2" placeholder="Last Name" type="text" />
      </div>
      <div class="first-name">
        <b class="first-name1">Email</b>
        <div class="first-name-child" />
        <input
          class="exampleemailcom2"
          placeholder="example.email.com"
          type="text"
        />
      </div>
      <div class="first-name">
        <b class="first-name1">Password</b>
        <div class="first-name-child" />
        <input class="password6" placeholder="Password" type="text" />
      </div>
      <div class="lets-get-in-touch1">
        <button class="sign-up5" :autoFocus="true">
          <div class="sign-up-item" />
          <button class="sign-up6" :autoFocus="true">Sign Up</button>
        </button>
      </div>
    </div>
    <div class="already-have-an">Already have an account?</div>
    <div class="makes-your-life-container">
      <p class="makes-your-life">Makes Your Life Easier!</p>
    </div>
    <div class="maximize-your-legal">
      Maximize your legal efficiency with our Paralegal AI Assistant. Upon
      understanding your firm's specific needs, our team will demonstrate how
      our AI can enhance your legal operations, from streamlining documentation
      to ensuring compliance with local regulations.
    </div>
    <img
      class="logo-2-icon"
      alt=""
      src="@/assets/logo.png"
      @click="onLogo2ImageClick"
    />
    <div class="sign-upsign-in">
      <div class="sign-in6" @click="onSignInTextClick">Sign In</div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SignUp",
    methods: {
      onTHEMISAITextClick() {
        this.$router.push("/home");
      },
      onLogo2ImageClick() {
        this.$router.push("/home");
      },
      onSignInTextClick() {
        this.$router.push("/sign-in");
      },
    },
  });
</script>
<style scoped>
  .themis-ai4 {
    position: absolute;
    top: 289px;
    left: 730px;
    line-height: 150%;
    display: inline-block;
    width: 351px;
    height: 58px;
    cursor: pointer;
  }
  .logonobackground-1-icon {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 1768px;
    height: 1047px;
    object-fit: cover;
    opacity: 0.3;
  }
  .logonobackground {
    position: absolute;
    top: -125px;
    left: -588px;
    width: 1768px;
    height: 1047px;
    text-align: center;
    font-size: var(--font-size-41xl);
    font-family: var(--font-saira);
  }
  .sign-up-child {
    position: absolute;
    top: 0px;
    left: 622px;
    background-color: var(--color-white);
    width: 818px;
    height: 815px;
  }
  .or1 {
    width: 37.4px;
    position: relative;
    font-weight: 500;
    display: inline-block;
    height: 36.8px;
    flex-shrink: 0;
  }
  .google-icon1 {
    width: 50px;
    position: relative;
    height: 50px;
    object-fit: cover;
  }
  .sign-in-with2 {
    position: relative;
    font-weight: 500;
  }
  .btn-google1 {
    flex: 1;
    border: 1.4px solid var(--color-darkslategray);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-7xs) var(--padding-base);
    gap: var(--gap-xs);
  }
  .facebook-icon1 {
    width: 51px;
    position: relative;
    height: 50px;
  }
  .sign-in-options1 {
    width: 607px;
    height: 58.5px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
    font-size: var(--paragraph-size);
  }
  .sign-in-google-fb1 {
    position: absolute;
    top: 654px;
    left: 727px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: 23px;
    font-size: var(--font-size-7xl);
    color: var(--color-darkslategray);
  }
  .sign-up4 {
    position: relative;
    font-size: var(--font-size-21xl);
    line-height: 120%;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .first-name1 {
    position: relative;
    line-height: 120%;
    z-index: 0;
  }
  .first-name-child {
    width: 517px;
    position: relative;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-darkslategray);
    box-sizing: border-box;
    height: 53px;
    mix-blend-mode: normal;
    z-index: 1;
  }
  .first-name2 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 248px;
    position: absolute;
    margin: 0 !important;
    top: 48.5px;
    left: 22.5px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    height: 21px;
    flex-shrink: 0;
    z-index: 2;
  }
  .first-name {
    width: 517px;
    height: 98px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    position: relative;
    gap: var(--gap-3xs);
  }
  .last-name2 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 248px;
    position: absolute;
    margin: 0 !important;
    top: 50.5px;
    left: 20.5px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    height: 21px;
    flex-shrink: 0;
    z-index: 2;
  }
  .exampleemailcom2 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 248px;
    position: absolute;
    margin: 0 !important;
    top: 50.5px;
    left: 21.5px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    height: 21px;
    flex-shrink: 0;
    z-index: 2;
  }
  .password6 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 248px;
    position: absolute;
    margin: 0 !important;
    top: 50.5px;
    left: 18.5px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    height: 21px;
    flex-shrink: 0;
    z-index: 2;
  }
  .sign-up-item {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-darkolivegreen);
    width: 132px;
    height: 48px;
  }
  .sign-up6 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 13px;
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
  .sign-up5 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    width: 132px;
    position: relative;
    height: 48px;
  }
  .lets-get-in-touch1 {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
  }
  .sign-up3 {
    position: absolute;
    top: 29px;
    left: 622px;
    width: 818px;
    height: 574px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 15px;
    color: var(--color-darkslategray);
    font-family: var(--paragraph);
  }
  .already-have-an {
    position: absolute;
    top: 615px;
    left: 867px;
    font-weight: 300;
    color: var(--color-black);
  }
  .makes-your-life {
    margin-block-start: 0;
    margin-block-end: 20px;
  }
  .makes-your-life-container {
    position: absolute;
    top: 239px;
    left: calc(50% - 646px);
    font-size: 50px;
    line-height: 150%;
    font-family: var(--font-anton);
    display: inline-block;
    width: 488px;
    height: 60px;
  }
  .maximize-your-legal {
    position: absolute;
    top: 341px;
    left: 39px;
    font-size: var(--font-size-xl);
    line-height: 200%;
    font-family: var(--font-raleway);
    text-align: center;
    display: inline-block;
    width: 557px;
    height: 200px;
  }
  .logo-2-icon {
    position: absolute;
    top: 5px;
    left: 33px;
    width: 81px;
    height: 88px;
    object-fit: cover;
    cursor: pointer;
  }
  .sign-in6 {
    position: relative;
    font-weight: 500;
    cursor: pointer;
  }
  .sign-upsign-in {
    position: absolute;
    top: 605px;
    left: 1099px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    text-align: center;
    color: var(--color-black);
  }
  .sign-up2 {
    width: 100%;
    position: relative;
    background: linear-gradient(180deg, #001429, #30411f);
    height: 815px;
    overflow: hidden;
    text-align: left;
    font-size: var(--font-size-lg);
    color: var(--color-white);
    font-family: var(--font-poppins);
  }
</style>
