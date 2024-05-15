<template>
  <div class="ai-system">
    <img class="ai-system-child" alt="" />
    <img class="mask-group-icon1" alt="" src="@/assets/mask-group@2x.png" />
    <div class="sign-in-sign-up1">
      <button class="sign-in1" :autoFocus="true">Sign In</button>
      <button class="sign-up2" :autoFocus="true">
        <div class="sign-up-item" />
        <button class="sign-up3" :autoFocus="true">Sign Up</button>
      </button>
    </div>
    <div class="logo-top1">
      <b class="themis-ai2" @click="onTHEMISAITextClick">THEMIS AI</b>
      <img
        class="logo-1-icon2"
        alt=""
        src="@/assets/logo.png"
        @click="onLogo1ImageClick"
      />
    </div>
    <div class="sidebar">
      <div class="sidebar-child" />
      <div class="new-chat">

        <b class="new-chat1">New Chat</b>
      </div>
      <div class="sidebar-inner">
        <div class="your-conversations-parent">
          <div class="your-conversations">Your conversations</div>
          <div class="clear-all">Clear All</div>
        </div>
      </div>
    </div>
    <div class="search-bar">
      <div class="search-bar-child" />
      <div class="vuesaxlinearsend-2-wrapper">
        <img
          class="vuesaxlinearsend-2-icon"
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
<style scoped>
  .ai-system-child {
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
  .mask-group-icon1 {
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
    font-family: var(--font-raleway);
    color: var(--color-gray-100);
    text-align: left;
    display: inline-block;
    opacity: 0.8;
  }
  .sign-up-item {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: var(--color-darkslategray);
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
    color: var(--color-white);
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
  .themis-ai2 {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
    cursor: pointer;
  }
  .logo-1-icon2 {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
    cursor: pointer;
  }
  .logo-top1 {
    position: absolute;
    top: 11px;
    left: 77px;
    width: 236px;
    height: 88px;
  }
  .sidebar-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: 26px;
    background-color: var(--color-gray-200);
    width: 253px;
    height: 687.2px;
  }
  .new-chat-child {
    position: absolute;
    top: calc(50% - 22.5px);
    left: calc(50% - 90px);
    border-radius: var(--br-3xs);
    width: 180px;
    height: 45px;
  }
  .new-chat1 {
    position: absolute;
    top: calc(50% - 13.6px);
    left: calc(50% - 73px);
    line-height: 150%;
    display: inline-block;
    width: 145px;
    height: 25.6px;
  }
  .new-chat {
    position: absolute;
    top: calc(50% - 320.2px);
    left: calc(50% - 89.5px);
    width: 180px;
    height: 45px;
  }
  .your-conversations {
    position: absolute;
    top: 0px;
    left: 0px;
    line-height: 20px;
    display: flex;
    align-items: center;
    width: 101px;
  }
  .clear-all {
    position: absolute;
    top: 0px;
    left: 161px;
    line-height: 20px;
    color: #5661f6;
    display: flex;
    align-items: center;
    width: 47px;
  }
  .your-conversations-parent {
    width: 208px;
    position: relative;
    height: 20px;
  }
  .sidebar-inner {
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
  .search-bar-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: var(--br-3xs);
    background-color: #fbfcff;
    width: 1041px;
    height: 47px;
  }
  .vuesaxlinearsend-2-icon {
    width: 24px;
    position: relative;
    height: 24px;
  }
  .vuesaxlinearsend-2-wrapper {
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
  .search-bar {
    position: absolute;
    top: 757px;
    left: 334px;
    width: 1041px;
    height: 47px;
  }
  .ai-system {
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
