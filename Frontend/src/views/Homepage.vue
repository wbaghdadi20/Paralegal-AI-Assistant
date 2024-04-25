<template>
  <div class="app-container">
    <el-container style="height: 100vh;">
      <el-header class="header">
        <div class="left-header">
          <img src="@/assets/logo.png" alt="Our Logo" class="logo" />
          <router-link to="/blog" class="nav-link">Blog</router-link>
          <router-link to="/ai-toolkits" class="nav-link">AI Toolkits</router-link>
        </div>
        <div class="right-header">
          <user-icon class="user-icon"></user-icon>
          <span v-if="login_true" @click="promptLogin">Log In</span> 
        </div>
      </el-header>
      <el-container>
        <el-aside width="200px" class="sidebar">
          <el-menu
            default-active="1"
            class="el-menu-vertical-demo"
            background-color="transparent"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="0">
              <router-link to="/">Home</router-link>
            </el-menu-item>
            <el-menu-item index="1" @click="startNewConversation">New Conversation</el-menu-item>
            <el-menu-item index="2" @click="navigateToConversation">Conversation List</el-menu-item>
            <el-menu-item index="3">Contact</el-menu-item>
          </el-menu>
        </el-aside>

        <el-main class="main-content">
          <div class="bottom-actions">
            <div class="action-grid">
              <el-card class="action-box" @click="startNewConversation">
                Start New Conversation
              </el-card>
              <el-card class="action-box" @click="navigateToConversation">
                Resume from Past Conversation
              </el-card>
              <el-card class="action-box">
                File Management
              </el-card>
              <el-card class="action-box">
                Contact Paralegal Expert
              </el-card>
            </div>
          </div>
        </el-main>

      </el-container>
    </el-container>
  </div>
</template>

<script>
import { User as UserIcon, ArrowRight } from '@element-plus/icons-vue';

export default {
  components: {
    'arrow-right': ArrowRight,
    'user-icon': UserIcon,
  },
  data() {
    return {
      searchQuery: '',
      conversation: [],
      login_true: true,
      showLoginPrompt: false,
    };
  },
  methods: {
    startNewConversation(event) {
      // this.saveConversationHistory();
      this.$router.push({ name: 'Newconversation' });
    },
    navigateToConversation(event) {
      this.$router.push({ name: 'Conversation' });
    },
    promptLogin() {
      this.showLoginPrompt = true;
    },
    onSearch() {
      if (this.login_true && this.searchQuery.trim()) {
        this.conversation.push({
          content: this.searchQuery,
          sender: 'user',
          date: new Date().toLocaleString(),
        });
        this.conversation.push({
          content: "Dummy GPT reply",
          sender: 'bot',
          date: new Date().toLocaleString(),
        });
        this.saveConversationHistory();
        this.searchQuery = '';
        this.scrollToBottom();
      }
    },
    // saveConversationHistory() {
    //   localStorage.setItem('conversationHistory', JSON.stringify(this.conversation));
    // },
    saveConversationHistory() {
      const combinedMessage = this.conversation.map(msg => `${msg.sender}: ${msg.content}`).join(' - ');
      localStorage.setItem('conversationHistory', JSON.stringify([{content: combinedMessage, date: new Date().toLocaleString()}]));
    },

    scrollToBottom() {
      this.$nextTick(() => {
        const container = this.$refs.conversationContainer;
        if (container) {
          container.scrollTop = container.scrollHeight;
        }
      });
    }
  },
  mounted() {
    const savedConversation = JSON.parse(localStorage.getItem('conversationHistory'));
    if (savedConversation) {
      this.conversation = savedConversation;
    }
  },
  watch: {
    conversation() {
      this.saveConversationHistory();
      this.scrollToBottom();
    },
  },
};
</script>


<!-- <style>
  .app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    color: white;
    padding: 0 20px;
  }

  .left-header, .right-header {
    display: flex;
    align-items: center;
  }

  .logo {
    height: 50px;
  }

  .nav-link {
    margin-left: 20px;
    color: white;
    text-decoration: none;
  }

  .user-icon {
    font-size: 24px;
    margin-right: 10px;
  }

  .sidebar {
    background-color: #092d54;
    width: 200px;
    overflow-y: auto;
  }

  .main-content {
    display: flex;
    flex-direction: column;
    height: 100%; 
    flex-grow: 1;
    overflow-y: hidden;
  }


  .title {
    font-size: 28px; 
    color: #4A90E2; 
    font-family: 'Arial', sans-serif; 
    margin-bottom: 20px;
  }

  .search-bar-container {
    display: flex;
    justify-content: center; 
    margin-bottom: 20px; /* Spacing at the bottom */
  }

  .search-bar {
    width: 100%;
    max-width: 800px;
    border-radius: 25px; 
    font-style: italic;
  }
  .send-button {
    border: none; 
    background: none; 
  }

  .conversation-section {
    flex-grow: 0;
    background-color: whitesmoke;
    padding: 10px;
    overflow-y: auto; 
    display: flex;
    flex-direction: column;
    height: 450px; 
  }

  .user {
    align-self: flex-end;
    background-color: #DCF8C6; 
  }

  .bot {
    align-self: flex-start; 
    background-color: #f0f8ff;
  }

  .conversation {
    flex-grow: 1; 
    margin: 20px 0;
    padding: 10px;
    background-color: #f0f8ff;
    border: 1px solid #ccc; 
    overflow-y: auto;
    width: 100%; 
  }
  .message-bubble {
    padding: 10px 20px;
    border-radius: 15px;
    margin: 10px 0;
    max-width: 50%; 
    word-wrap: break-word; 
  }

  .contact-page {
    text-align: center;
  }

</style> -->
<style>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: white;
  padding: 0 20px;
}

.left-header, .right-header {
  display: flex;
  align-items: center;
}

.logo {
  height: 50px;
}

.nav-link {
  margin-left: 20px;
  color: white;
  text-decoration: none;
}

.user-icon {
  font-size: 24px;
  margin-right: 10px;
}

.sidebar {
  background-color: #092d54;
  width: 200px;
  overflow-y: auto;
}

.main-content {
  flex-grow: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.bottom-actions {
  margin-top: auto;
  padding: 20px;
  width: 100%;
  position: absolute;
  bottom: 0;
  height: 25%;
}

.action-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 40px;
  height: 100%;
  padding: 0 20%;
}

.action-box {
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  text-align: center;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  transition: background-color 0.3s, transform 0.2s;
  height: 100%;
  background-color: #f5f5f5;
}

.action-box:hover {
  background-color: #e6e6e6;
  transform: translateY(-2px);
}
</style>


