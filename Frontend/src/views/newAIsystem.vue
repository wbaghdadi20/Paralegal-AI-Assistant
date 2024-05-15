<template>
  <div :class="$style.aiSystem">
    <img :class="$style.aiSystemChild" alt="" />
    <img :class="$style.maskGroupIcon" alt="" src="@/assets/mask-group@2x.png" />
    <div :class="$style.signInSignUp">
      <button :class="$style.signIn" :autoFocus="true">Sign In</button>
      <button :class="$style.signUp" :autoFocus="true">
        <div :class="$style.signUpChild" />
        <button :class="$style.signUp1" :autoFocus="true">Sign Up</button>
      </button>
    </div>
    <div :class="$style.logoTop">
      <b :class="$style.themisAi" @click="onTHEMISAITextClick">THEMIS AI</b>
      <img :class="$style.logo1Icon" alt="" src="@/assets/logo.png" @click="onLogo1ImageClick"/>
    </div>
    <div :class="$style.sidebar">
      <div :class="$style.sidebarChild" />
      <div :class="$style.newChat">
        <div :class="$style.signUpChild" />
        <button :class="$style.signUp1" :autoFocus="true">New Chat</button>
        <b :class="$style.newChat1">New Chat</b>
      </div>
      <div :class="$style.sidebarInner">
        <div :class="$style.yourConversationsParent">
          <div :class="$style.yourConversations">Your conversations</div>
          <div :class="$style.clearAll">Clear All</div>
        </div>
      </div>
    </div>
    <div :class="$style.searchBar">
      <div :class="$style.searchBarChild" />
      <div :class="$style.vuesaxlinearsend2Wrapper">
        <img
          :class="$style.vuesaxlinearsend2Icon"
          alt=""
          src="@/assets/vuesaxlinearsend2.png"
        />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "AISystem",
    methods: {
      onTHEMISAITextClick() {
        this.$router.push("/");
      },
      onLogo1ImageClick() {
        this.$router.push("/");
      },
    },
  });
</script>

<style module>
  .aiSystemChild {
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
    height: 143.03%;
    width: 81.13%;
    top: -65.1%;
    right: 9.41%;
    bottom: 22.07%;
    left: 9.47%;
    max-width: 100%;
    overflow: hidden;
    max-height: 100%;
    object-fit: contain;
    display: none;
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
  .themisAi {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
    cursor: pointer;
  }
  .logo1Icon {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
    cursor: pointer;
  }
  .logoTop {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
  }
  .sidebarChild {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: 26px;
    background-color: var(--color-gray-200);
    width: 253px;
    height: 687.2px;
  }
  .newChatChild {
    position: absolute;
    top: calc(50% - 22.5px);
    left: calc(50% - 90px);
    border-radius: var(--br-3xs);
    width: 180px;
    height: 45px;
  }
  .newChat1 {
    position: absolute;
    top: calc(50% - 13.6px);
    left: calc(50% - 73px);
    line-height: 150%;
    display: inline-block;
    width: 145px;
    height: 25.6px;
  }
  .newChat {
    position: absolute;
    top: calc(50% - 320.2px);
    left: calc(50% - 89.5px);
    width: 180px;
    height: 45px;
  }
  .yourConversations {
    position: absolute;
    top: 0px;
    left: 0px;
    line-height: 20px;
    display: flex;
    align-items: center;
    width: 101px;
  }
  .clearAll {
    position: absolute;
    top: 0px;
    left: 161px;
    line-height: 20px;
    color: #5661f6;
    display: flex;
    align-items: center;
    width: 47px;
  }
  .yourConversationsParent {
    width: 208px;
    position: relative;
    height: 20px;
  }
  .sidebarInner {
    position: absolute;
    top: 83px;
    left: 7px;
    width: 223px;
    height: 15.5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: left;
    font-size: var(--font-size-sm);
    color: #6a6a6a;
  }
  .sidebar {
    position: absolute;
    top: 116.8px;
    left: 44px;
    width: 253px;
    height: 687.2px;
    font-size: var(--font-size-lg);
    color: var(--color-white);
  }
  .searchBarChild {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: #fbfcff;
    width: 1041px;
    height: 47px;
  }
  .vuesaxlinearsend2Icon {
    width: 24px;
    position: relative;
    height: 24px;
  }
  .vuesaxlinearsend2Wrapper {
    position: absolute;
    top: 6px;
    left: 997px;
    box-shadow: 0px 4px 8px rgba(86, 97, 246, 0.25);
    border-radius: 60px;
    background-color: var(--color-darkslategray);
    width: 36px;
    height: 36px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 10px;
    box-sizing: border-box;
  }
  .searchBar {
    position: absolute;
    top: 757px;
    left: 334px;
    width: 1041px;
    height: 47px;
  }
  .aiSystem {
    width: 100%;
    position: relative;
    background-color: var(--color-ghostwhite);
    height: 815px;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-xl);
    color: var(--color-black);
    font-family: var(--font-raleway);
  }
</style>
