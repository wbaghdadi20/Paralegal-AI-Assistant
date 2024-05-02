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
              background-color="transparent"
              text-color="#fff">
              <el-menu-item index="0" @click="navigateToHome">Home</el-menu-item>
              <el-menu-item index="1" @click="startNewConversation">New Conversation</el-menu-item>
              <el-menu-item index="2" @click="navigateToConversation">Conversation List</el-menu-item>
              <el-menu-item index="3">Contact</el-menu-item>
            </el-menu>
          </el-aside>
  
          <el-main class="main-content">
            <div class="contact-page" style="margin-top: 0px;">
              <h1 class="title">Paralegal Assistance: Talk to us</h1>
            </div>
            
            <div class="conversation-section" ref="conversationContainer">
              <div v-for="(message, index) in conversation" :key="index" 
                  class="message-bubble" :class="{'user': message.sender === 'user', 'bot': message.sender === 'bot'}">
                {{ message.content }}
              </div>
            </div>
            <div class="search-bar-container">
                <el-input v-model="searchQuery" placeholder="Enter your query..." @keyup.enter="onSearch" class="search-bar">
                    <template #suffix>
                    <el-button icon="el-icon-upload" class="upload-button" @click="promptFileUpload" style="background: none; border: none;"></el-button>
                    </template>
                </el-input>
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
        uploadedFile: null,
        login_true: true,
        showLoginPrompt: false,
      };
    },
    methods: {
        navigateToHome(event) {
            this.$router.push({ name: 'homepage' });
        },
        navigateToConversation(event) {
            this.$router.push({ name: 'Conversation' });
        },
        promptLogin() {
            this.showLoginPrompt = true;
        },
        async handleSubmit() {
          this.loading = true;
          try {
            const questionContent = this.searchQuery;
            if (this.uploadedFile) {
              // Handle file upload with FormData
              const formData = new FormData();
              formData.append('file', this.uploadedFile);
              formData.append('query', this.searchQuery);

              const response = await fetch('http://127.0.0.1:5001/askQuestion', {
                method: 'POST',
                body: formData, // FormData will set the correct Content-Type header
              });
              const data = await response.text(); // Assuming the response is JSON
              this.conversation.push({
                content: data, // Assuming 'answer' is the key in the JSON response
                sender: 'bot',
                date: new Date().toLocaleString(),
              });
            }
            else{
              const response = await fetch('http://127.0.0.1:5001/askQuestion', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: questionContent })
              });
              const data = await response.text(); // Assuming the response is text
              this.conversation.push({
                content: data,
                sender: 'bot',
                date: new Date().toLocaleString(),
              });
            }
          } catch (error) {
            console.error('Error:', error);
            this.conversation.push({
              content: 'An error occurred. Please try again.',
              sender: 'bot',
              date: new Date().toLocaleString(),
            });
          } finally {
            this.loading = false;
            this.searchQuery = ''; // Clear the search query after the response
            this.scrollToBottom();
          }
        },
        onSearch() {
          if (this.login_true && (this.searchQuery.trim() || this.uploadedFile)) { 
              this.conversation.push({
              content: this.searchQuery,
              sender: 'user',
              date: new Date().toLocaleString(),
              });

              this.handleSubmit(); // Call handleSubmit to process the question


              this.saveConversationHistory();
              this.searchQuery = '';
              this.scrollToBottom();
          }
        },
        // onSearch() {
        //   if (this.login_true && this.searchQuery.trim()) {
        //       this.conversation.push({
        //       content: this.searchQuery,
        //       sender: 'user',
        //       date: new Date().toLocaleString(),
        //       });
        //       this.conversation.push({
        //       content: "Dummy GPT reply",
        //       sender: 'bot',
        //       date: new Date().toLocaleString(),
        //       });
        //       this.saveConversationHistory();
        //       this.searchQuery = '';
        //       this.scrollToBottom();
        //   }
        // },
      // saveConversationHistory() {
      //   localStorage.setItem('conversationHistory', JSON.stringify(this.conversation));
      // },
        // saveConversationHistory() {
        //   const combinedMessage = this.conversation.map(msg => `${msg.sender}: ${msg.content}`).join(' - ');
        //   localStorage.setItem('conversationHistory', JSON.stringify([{content: combinedMessage, date: new Date().toLocaleString()}]));
        // },
        saveConversationHistory() {
          // Filter the conversation array to include only messages sent by 'user'
          const combinedMessage = this.conversation
            .filter(msg => msg.sender === 'user')  // Only include messages from 'user'
            .map(msg => `${msg.sender}: ${msg.content}`)  // Map each message to a string
            .join(' - ');  // Join all messages into a single string with separators

          // Store the combined message in local storage with the current date and time
          localStorage.setItem('conversationHistory', JSON.stringify([{content: combinedMessage, date: new Date().toLocaleString()}]));
        },


        // promptFileUpload() {
        //     let fileInput = document.createElement('input');
        //     fileInput.type = 'file';
        //     fileInput.style.display = 'none'; // Hide the input element
        //     fileInput.onchange = e => {
        //         let file = fileInput.files[0];
        //         if (file) {
        //         // Calculate file size in MB
        //           const fileSize = (file.size / 1024 / 1024).toFixed(2) + ' MB';
        //         // Construct file data message
        //           const fileData = {
        //               content: `File uploaded: ${file.name}, Size: ${fileSize}, Type: ${file.type}`,
        //               sender: 'user',
        //               date: new Date().toLocaleString(),
        //               status: 'Upload successful'
        //           };
        //           this.conversation.push(fileData);
        //           this.saveConversationHistory();
        //           this.scrollToBottom();
        //         }
        //     };
        //     document.body.appendChild(fileInput);
        //     fileInput.click();
        //     document.body.removeChild(fileInput); // Clean up after adding
        // },
        promptFileUpload() {
          let fileInput = document.createElement('input');
          fileInput.type = 'file';
          fileInput.style.display = 'none'; // Hide the input element
          fileInput.onchange = e => {
            this.uploadedFile = e.target.files[0];  // Store the file object
            if (this.uploadedFile) {
              this.conversation.push({
                content: `File ready to upload: ${this.uploadedFile.name}`,
                sender: 'user',
                date: new Date().toLocaleString(),
              });
            }
            document.body.removeChild(fileInput); // Clean up by removing the file input
          };
          document.body.appendChild(fileInput);
          fileInput.click();
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
  
  
  <style>
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
  
    /* .search-bar-container {
      display: flex;
      justify-content: center; 
      margin-bottom: 20px; 
    } */
  
    /* .search-bar {
      width: 100%;
      max-width: 800px;
      border-radius: 25px; 
      font-style: italic;
    } */

    .search-bar-container {
        display: flex;
        justify-content: center; 
        margin-bottom: 20px; 
    }

    .search-bar {
        width: 100%;
        max-width: 800px;
        height: 50px; 
        border-radius: 25px; 
        font-style: italic;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2); 
        padding: 0 20px; 
    }

    

    .upload-button {
        cursor: pointer;
        color: #606266; /* Changed to be more visible, adjust as needed */
        font-size: 20px; /* Ensure icon size is sufficient */
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
  
  </style>