<template>
  <el-container style="height: 100vh;">
    <el-aside width="200px" class="sidebar">
      <!-- Sidebar content -->
      <el-menu
        default-active="1"
        class="el-menu-vertical-demo"
        background-color="transparent"
        text-color="#faf"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="1">
          <router-link to="/">Home</router-link>
        </el-menu-item>
        <el-menu-item index="2">Conversation List</el-menu-item>
        <el-menu-item index="3">Contact</el-menu-item>
      </el-menu>
    </el-aside>

    <el-main>
      <div class="contact-page">
        <h1 class="title">Talk to us</h1>
        <div class="search-bar-container">
          <form @submit.prevent="onSearch">
            <input
              type="text"
              v-model="searchQuery"
              placeholder="Enter your query..."
              class="search-bar"
              required
            />
          </form>
        </div>

        <div
          class="file-drop-area"
          @dragover.prevent="handleDragOver"
          @dragleave.prevent="handleDragLeave"
          @drop.prevent="handleFileDrop"
        >
          Drag files here to upload
        </div>

        <div v-if="conversation.length > 0" class="conversation">
          <div v-for="(message, index) in conversation" :key="index" class="message-container">
            <div :class="{'user-message': message.sender === 'user', 'bot-message': message.sender === 'bot'}">
              <span :class="{'user-dot': message.sender === 'user', 'bot-dot': message.sender === 'bot'}"></span>
              {{ message.content }}
            </div>
          </div>
          <button @click="clearConversation" class="clear-button">Clear</button>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      conversation: [],
    };
  },
  methods: {
    async onSearch() {
      this.conversation.push({ content: this.searchQuery, sender: 'user' });

      const url = 'http://127.0.0.1:5000/askQuestion';
      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ question: this.searchQuery }),
        });

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.text(); 


        console.log('Response from servers: ', data);
        this.conversation.push({ content: data.message, sender: 'bot' });
      } catch (error) {
        console.error('Error:', error);
        this.conversation.push({ content: 'Sorry, there was an error processing your request.', sender: 'bot' });
      }

      this.searchQuery = '';
    },
    handleDragOver(event) {
      event.target.style.backgroundColor = '#add8e6';
    },
    handleDragLeave(event) {
      event.target.style.backgroundColor = '';
    },
    handleFileDrop(event) {
      const files = event.dataTransfer.files;
      if (files.length > 0) {
        console.log('Dropped files', files);
      }
      event.target.style.backgroundColor = '';
    },
    clearConversation() {
      this.conversation = [];
    },
  },
};
</script>

<style>
.contact-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
.title {
  font-size: 32px;
  margin-bottom: 20px;
  text-align: center;
}
.search-bar-container {
  width: 100%;
  max-width: 500px;
}
.search-bar {
  width: 100%;
  padding: 12px 15px;
  font-size: 16px;
  border: 2px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}
.conversation {
  width: 100%;
  max-width: 500px;
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  overflow-y: auto;
  background-color: #fafafa;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.user-message, .bot-message {
  padding: 8px 10px;
  border-radius: 10px;
  margin: 5px 0;
  word-wrap: break-word;
}
.user-message {
  align-self: flex-end;
  background-color: #e0e0e0;
}
.bot-message {
  align-self: flex-start;
  background-color: #f0f0f0;
}
.clear-button {
  padding: 8px 15px;
  margin-top: 10px;
  background-color: #f44336;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.clear-button:hover {
  background-color: #d32f2f;
}
.file-drop-area {
  border: 2px dotted #ccc;
  padding: 20px;
  text-align: center;
  color: #ccc;
  margin: 20px auto;
  width: 90%;
  height: 200px; 
  background-color: #f0f8ff; 
  cursor: pointer;
}
</style>
