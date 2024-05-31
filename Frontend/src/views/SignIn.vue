<template>
  <div class="sign-in1">
    <div class="sign-in-child" />
    <div class="sign-in2">
      <div class="sign-in3">
        <b class="sign-in4">Sign In</b>
        <div class="password">
          <b class="email2">Email</b>
          <input class="email-child" type="text" />
          <input
            class="exampleemailcom1"
            placeholder="example@email.com"
            type="text"
          />
        </div>
        <div class="password">
          <b class="password1">
            <p class="password2">Password</p>
          </b>
          <div class="password-child" />
          <input class="password3" placeholder="Password" type="text" />
        </div>
        <button class="sign-in-sign-in" :autoFocus="true">
          <img class="sign-in-sign-in-child" alt="" src="@/assets/signInRectangle.png" />
          <button class="sign-in5" :autoFocus="true">Sign In</button>
        </button>
      </div>
    </div>
    <div class="sign-in-google-fb">
      <div class="sign-in-options">
        <div class="btn-google">
          <img class="google-icon" alt="" src="@/assets/Google.png" />
          <div class="sign-in-with">Sign in with Google</div>
        </div>
        <div class="btn-google">
          <img class="facebook-icon" alt="" src="@/assets/Facebook.png" />
          <div class="sign-in-with">Sign in with Facebook</div>
        </div>
      </div>
      <div class="or">OR</div>
    </div>
    <div class="logo-top2" @click="onLogoTopContainerClick">
      <b class="themis-ai3">THEMIS AI</b>
      <img class="logo-1-icon3" alt="" src="@/assets/logo.png" />
    </div>
    <div class="create-an-account1">
      <div class="create-an-account2" @click="onCreateAnAccountClick">
        create an account
      </div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "SignIn",
    methods: {
      onLogoTopContainerClick() {
        this.$router.push("/home");
      },
      onCreateAnAccountClick() {
        this.$router.push("/sign-up");
      },
    },
  });
</script>
<style scoped>
  .sign-in-child {
    position: absolute;
    top: calc(50% - 375.5px);
    left: calc(50% - 675px);
    border-radius: var(--br-8xs);
    background-color: var(--color-white);
    width: 1350px;
    height: 750px;
  }
  .sign-in4 {
    width: 298px;
    position: relative;
    font-size: var(--font-size-21xl);
    line-height: 120%;
    display: inline-block;
    font-family: var(--font-raleway);
    text-align: center;
  }
  .email2 {
    width: 68px;
    position: relative;
    line-height: 120%;
    display: inline-block;
    z-index: 0;
  }
  .email-child {
    border: 1px solid var(--color-black);
    outline: none;
    background-color: transparent;
    width: 517px;
    position: relative;
    border-radius: var(--br-3xs);
    box-sizing: border-box;
    height: 53px;
    mix-blend-mode: normal;
    z-index: 1;
  }
  .exampleemailcom1 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 245px;
    position: absolute;
    margin: 0 !important;
    top: 48px;
    left: 20px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    z-index: 2;
  }
  .password2 {
    margin: 0;
  }
  .password1 {
    width: 140px;
    position: relative;
    line-height: 120%;
    display: inline-block;
    height: 22px;
    flex-shrink: 0;
    z-index: 0;
  }
  .password-child {
    width: 517px;
    position: relative;
    border-radius: var(--br-3xs);
    border: 1px solid var(--color-black);
    box-sizing: border-box;
    height: 53px;
    mix-blend-mode: normal;
    z-index: 1;
  }
  .password3 {
    border: none;
    outline: none;
    font-family: var(--paragraph);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 116px;
    position: absolute;
    margin: 0 !important;
    top: 49px;
    left: 24px;
    line-height: 150%;
    color: var(--color-black);
    text-align: left;
    display: inline-block;
    z-index: 2;
  }
  .password {
    width: 517px;
    height: 102px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    position: relative;
    gap: var(--gap-3xs);
  }
  .sign-in-sign-in-child {
    width: 132px;
    position: relative;
    border-radius: var(--br-3xs);
    height: 48px;
    z-index: 0;
  }
  .sign-in5 {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    width: 60px;
    position: absolute;
    margin: 0 !important;
    top: 12px;
    left: 36px;
    font-size: var(--paragraph-size);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
    display: inline-block;
    z-index: 1;
  }
  .sign-in-sign-in {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    position: relative;
    gap: var(--gap-3xs);
  }
  .sign-in3 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 818px;
    height: 428px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
    gap: 25px;
  }
  .sign-in2 {
    position: absolute;
    top: 99px;
    left: 311px;
    width: 818px;
    height: 428px;
  }
  .google-icon {
    width: 50px;
    position: relative;
    height: 50px;
    object-fit: cover;
  }
  .sign-in-with {
    position: relative;
    font-weight: 500;
  }
  .btn-google {
    flex: 1;
    border: 1.4px solid var(--color-darkslategray);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: var(--padding-7xs) var(--padding-base);
    gap: var(--gap-xs);
  }
  .facebook-icon {
    width: 51px;
    position: relative;
    height: 50px;
  }
  .sign-in-options {
    position: absolute;
    top: 63px;
    left: 0px;
    width: 600px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: flex-start;
    gap: var(--gap-5xl);
  }
  .or {
    position: absolute;
    top: 0px;
    left: 282px;
    font-size: var(--font-size-7xl);
    font-weight: 500;
  }
  .sign-in-google-fb {
    position: absolute;
    top: 572px;
    left: 420px;
    width: 600px;
    height: 125px;
    font-size: var(--paragraph-size);
    font-family: var(--font-poppins);
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
  .logo-top2 {
    position: absolute;
    top: 38px;
    left: 60px;
    width: 236px;
    height: 88px;
    cursor: pointer;
    text-align: center;
    font-size: var(--font-size-xl);
    color: var(--color-black);
    font-family: var(--font-saira);
  }
  .create-an-account2 {
    position: relative;
    line-height: 120%;
    font-weight: 500;
    cursor: pointer;
  }
  .create-an-account1 {
    position: absolute;
    top: 519px;
    left: 632px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    text-align: center;
  }
  .sign-in1 {
    width: 100%;
    position: relative;
    background: linear-gradient(180deg, #001429, #31421f);
    height: 815px;
    overflow: hidden;
    text-align: left;
    font-size: var(--font-size-lg);
    color: var(--color-darkslategray);
    font-family: var(--paragraph);
  }
</style>
