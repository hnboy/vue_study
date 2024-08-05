<template>
  <el-container class="layout-container-start_page" style="height: 1080px">
    <el-aside width="200px">
      <el-scrollbar>
        <el-menu :default-openeds="['1', '3']">
          <el-sub-menu index="1">
            <template #title>
              <el-icon><Tools /></el-icon>ToolBox
            </template>
             <el-menu-item-group>
              <template #title>Group 1</template>
              
              <el-menu-item index="1-1" @click="handleItemClick('wafer_map')">Option 1</el-menu-item>

              <el-menu-item index="1-2" @click="handleItemClick('address_convert')">Option 2</el-menu-item>

              <el-menu-item index="1-3" @click="handleItemClick('tb_yield')">Option 3</el-menu-item>

            <el-menu-item index="1-4" @click="handleItemClick('vt_chart')">Option 4</el-menu-item>
            </el-menu-item-group>
          </el-sub-menu>
        </el-menu>
      </el-scrollbar>
    </el-aside>

    <el-container>
      <el-header style="text-align: center; font-size: 12px">
        <div class="toolbar">
          <span>ZZWS</span>
        </div>
      </el-header>

      <el-main>
        <WaferMap v-if="activeComponent === 'wafer_map'" /> <!-- 注意这里 -->
        <Address v-if="activeComponent === 'address_convert'" /> <!-- 注意这里 -->
        <Yield v-if="activeComponent === 'tb_yield'" /> <!-- 注意这里 -->
        <VT v-if="activeComponent === 'vt_chart'" /> <!-- 注意这里 -->
        
        <!--显示项目良率信息 -->
      </el-main>
    </el-container>
  </el-container>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { Menu as IconMenu, Tools, Setting } from '@element-plus/icons-vue'

import WaferMap from './component/wafer.vue';
import Address from './component/address.vue';
import Yield from './component/yield.vue';
import VT from './component/vt.vue';

const item = {
  date: '2024-05-02',
}
const tableData = ref(Array.from({ length: 10 }).fill(item))
const activeComponent = ref('Component1'); // 设置初始值


const handleItemClick = (componentName: string) => {

  activeComponent.value = componentName;

};
</script>

<style scoped>
.layout-container-demo .el-header {
  position: relative;
  background-color: var(--el-color-primary-light-7);
  color: var(--el-text-color-primary);
}
.layout-container-demo .el-aside {
  color: var(--el-text-color-primary);
  background: var(--el-color-primary-light-8);
}
.layout-container-demo .el-menu {
  border-right: none;
}
.layout-container-demo .el-main {
  padding: 0;
}
.layout-container-demo .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  right: 20px;
}
</style>

