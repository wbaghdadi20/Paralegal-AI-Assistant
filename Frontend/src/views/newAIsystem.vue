<template>
  <div class="ai-system">
    <div class="logo-top">
      <b class="themis-ai" @click="onTHEMISAITextClick">THEMIS AI</b>
      <img
        class="logo-1-icon"
        alt=""
        src="@/assets/logo.png"
        @click="onLogo1ImageClick"
      />
    </div>
    <div class="sidebar">
      <div class="sidebar-child" />
      <div class="new-chat">
        <img class="new-chat-child" alt="" src="@/assets/newchatbar.png" />
        <button class="new-chat1">New Chat</button>
      </div>
      <div class="your-conversations-clear-all">
        <div class="your-conversations-parent">
          <div class="your-conversations">Your conversations</div>
          <button class="clear-all">Clear All</button>
        </div>
      </div>
    </div>
    <div class="search-bar">
      <input
        class="ask-paralegal-ai"
        placeholder="ask Paralegal AI Assistent"
        type="text"
      />
      <div class="vuesaxlinearsend-2-wrapper">
        <img
          class="vuesaxlinearsend-2-icon"
          alt=""
          src="@/assets/send.png"
        />
      </div>
    </div>
  </div>
</template>
<script>
  import { defineComponent } from "vue";

  export default defineComponent({
    name: "AISystem",
    methods: {
      onTHEMISAITextClick() {
        this.$router.push("/home");
      },
      onLogo1ImageClick() {
        this.$router.push("/home");
      },
    },
  });
</script>
<style scoped>
  .themis-ai {
    position: absolute;
    top: 28px;
    left: 39px;
    line-height: 150%;
    display: inline-block;
    width: 197px;
    height: 29px;
    cursor: pointer;
  }
  .logo-1-icon {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 81px;
    height: 88px;
    object-fit: cover;
    cursor: pointer;
  }
  .logo-top {
    position: absolute;
    top: 11px;
    left: 61px;
    width: 236px;
    height: 88px;
  }
  .sidebar-child {
    position: absolute;
    top: 0px;
    left: 0px;
    border-radius: 26px;
    background-color: var(--color-white);
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
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: calc(50% - 13.6px);
    left: calc(50% - 73px);
    font-size: var(--font-size-lg);
    line-height: 150%;
    font-weight: 700;
    font-family: var(--font-raleway);
    color: var(--color-white);
    text-align: center;
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
    font-weight: 500;
    display: flex;
    align-items: center;
    width: 135px;
  }
  .clear-all {
    cursor: pointer;
    border: none;
    padding: 0;
    background-color: transparent;
    position: absolute;
    top: 0px;
    left: 161.8px;
    font-size: var(--font-size-sm);
    line-height: 20px;
    font-weight: 500;
    font-family: var(--font-raleway);
    color: #5661f6;
    text-align: left;
    display: flex;
    align-items: center;
    width: 65px;
  }
  .your-conversations-parent {
    width: 226.8px;
    position: relative;
    height: 20px;
  }
  .your-conversations-clear-all {
    position: absolute;
    top: 83px;
    left: 7px;
    width: 223px;
    height: 15.5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
  }
  .sidebar {
    position: absolute;
    top: 103.8px;
    left: 44px;
    width: 253px;
    height: 687.2px;
    text-align: left;
    font-size: var(--font-size-sm);
    color: #6e6e6e;
    font-family: var(--font-raleway);
  }
  .ask-paralegal-ai {
    border: none;
    outline: none;
    font-family: var(--font-raleway);
    font-size: var(--font-size-sm);
    background-color: transparent;
    width: 971px;
    position: relative;
    line-height: 20px;
    color: rgba(0, 0, 0, 0.39);
    text-align: left;
    display: flex;
    align-items: center;
    height: 33px;
    flex-shrink: 0;
  }
  .vuesaxlinearsend-2-icon {
    width: 24px;
    position: relative;
    height: 24px;
  }
  .vuesaxlinearsend-2-wrapper {
    width: 36px;
    box-shadow: 0px 4px 8px rgba(86, 97, 246, 0.25);
    border-radius: 60px;
    background-color: var(--color-darkslategray);
    height: 36px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: var(--padding-3xs);
    box-sizing: border-box;
  }
  .search-bar {
    position: absolute;
    top: 751px;
    left: 334px;
    border-radius: var(--br-3xs);
    background-color: #fbfcff;
    width: 1034px;
    height: 46px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    padding: 5px 8px;
    box-sizing: border-box;
    gap: 11px;
  }
  .ai-system {
    width: 100%;
    position: relative;
    background-color: var(--color-gray-100);
    height: 815px;
    overflow: hidden;
    text-align: center;
    font-size: var(--font-size-xl);
    color: var(--color-white);
    font-family: var(--font-saira);
  }
</style>
