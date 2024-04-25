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
        <!-- <el-aside width="200px" class="sidebar">
          <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            background-color="transparent"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="1">
              <router-link to="/">Home</router-link>
            </el-menu-item>
            <el-menu-item index="2" @click="navigateToConversation">Conversation List</el-menu-item>
            <el-menu-item index="3">Contact</el-menu-item>
          </el-menu>
        </el-aside> -->
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
            <el-menu-item index="1">
              <router-link to="/newconversation">New Conversation</router-link>
            </el-menu-item>
            <!-- @click="startNewConversation">New Conversation</el-menu-item> -->
            <el-menu-item index="2" @click="navigateToConversation">Conversation List</el-menu-item>
            <el-menu-item index="3">Contact</el-menu-item>
          </el-menu>
        </el-aside>
        <el-main class="main-content">
          <el-table :data="tableData" style="width: 100%">
            <el-table-column
              label="Created Time"
              width="180"
              prop="date">
              <template v-slot="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.date }}</span>
              </template>
            </el-table-column>
            <el-table-column label="Conversation" prop="content" width="600">
              <template v-slot="scope">
                {{ limitWords(scope.row.content, 15) }}
              </template>
            </el-table-column>
            <el-table-column label="Actions">
              <template v-slot="scope">
                <el-button
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)">Manage</el-button>
                <el-button
                  size="mini"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>


<script>
import { User as UserIcon } from '@element-plus/icons-vue';

export default {
  components: {
    'user-icon': UserIcon
  },
  data() {
    return {
      tableData: [],
      login_true: true,
    };
  },
  methods: {
    startNewConversation(event) {
      this.$router.push({ name: 'Newconversation' });
    },
    limitWords(text, limit) {
      const words = text.split(/\s+/);
      if (words.length > limit) {
        return words.slice(0, limit).join(' ') + '...';
      }
      return text;
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      this.tableData.splice(index, 1);
      localStorage.setItem('conversationHistory', JSON.stringify(this.tableData));
    }
  },
  // mounted() {
  //   const savedConversation = JSON.parse(localStorage.getItem('conversationHistory'));
  //   if (savedConversation) {
  //     this.tableData = savedConversation;
  //   }
  // },
  mounted() {
    const savedConversation = JSON.parse(localStorage.getItem('conversationHistory'));
    if (savedConversation && savedConversation.length > 0) {
      this.tableData = savedConversation;
    }
  },

};
</script>



<style>
  .app-container {
      display: flex;
      flex-direction: column;
      height: 100vh;
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
      background-color: #f4f4f4;
  }

  .contact-page, .title, .search-bar-container, .file-drop-area, .conversation, .clear-button {
      margin: 20px;
  }

  .search-bar {
      width: 100%;
      padding: 12px 15px;
  }

  .file-drop-area {
      background-color: #f0f8ff;
      padding: 20px;
      border: 2px dotted #ccc;
  }

  .conversation {
      max-width: 500px;
  }

  .clear-button {
      background-color: #f44336;
      color: white;
      padding: 8px 15px;
      border-radius: 4px;
      cursor: pointer;
  }

  .clear-button:hover {
      background-color: #d32f2f;
  }

  .user-message, .bot-message {
      padding: 8px 10px;
      border-radius: 10px;
      margin: 5px 0;
  }

  .el-table .warning-row {
      background: oldlace;
  }

  .el-table .success-row {
      background: #f0f9eb;
  }

</style>