<template>
  <div>
    <el-upload
      class="upload-demo"
      drag
      action=""
      :on-change="handleFileChange"
      :auto-upload="false"
      :show-file-list="false"
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    </el-upload>
    <div v-if="waferImage">
      <img :src="waferImage" alt="Wafer Map" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue';
import * as Papa from 'papaparse';

// 存储 Wafer Map 图像的 URL
const waferImage = ref('');

// 处理文件改变的函数
const handleFileChange = (file, fileList) => {
  // 读取文件内容
  const reader = new FileReader();
  reader.onload = () => {
    const csvData = reader.result;
    parseCSV(csvData);
  };
  reader.readAsText(file.raw);
};

// 解析 CSV 文件数据
const parseCSV = (data) => {
  Papa.parse(data, {
    header: true,
    complete: function(results) {
      // results.data 包含解析后的数据
      generateWaferMap(results.data);
    },
  });
};

// 生成 Wafer Map 图像
const generateWaferMap = async (data) => {
  try {
    // 假设 data 中有必要的数据格式来生成 Wafer Map
    // 这里我们使用一个假设的数据结构
    const waferMapPrompt = createWaferMapPrompt(data);
    const imageResponse = await generateWaferMapImage(waferMapPrompt);
    waferImage.value = imageResponse;
  } catch (error) {
    console.error('Error generating Wafer Map:', error);
  }
};

// 创建 Wafer Map 的描述
const createWaferMapPrompt = (data) => {
  // 假设 data 中有必要的信息来描述 Wafer Map
  return `Wafer: ${JSON.stringify(data)}`;
};

// 调用 API 生成 Wafer Map 图像
const generateWaferMapImage = async (prompt) => {
  const response = await fetch('http://localhost:8000/api/wafer-map', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ prompt }),
  });

  if (!response.ok) {
    throw new Error(`Failed to generate Wafer Map: ${response.statusText}`);
  }

  const imageData = await response.json();
  return imageData.image_url;
//  return await response.blob().then(blob => URL.createObjectURL(blob));
};

// 初始化时加载
onMounted(() => {
  // 初始化操作，如果有需要的话
});
</script>

<style scoped>
.upload-demo {
  width: 50%;
  margin: 0 auto;
}
</style>