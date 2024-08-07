<template>
   <div class="input" > 

   <span class="blk"> blk: </span>
   <el-input-number v-model="blk" :controls="false" :min="0" :max="0xFFFFFFFFFF" @change="handleChange" />

   <span class="wl"> wl: </span>
   <el-input-number v-model="wl" :controls="false" :min="0" :max="0xFFFFFFFFFF" @change="handleChange" />

   <span class="string"> string:  </span>
   <el-input-number v-model="string" :controls="false" :min="0" :max="0xFFFFFFFFFF" @change="handleChange" />
   </div>

   <div class="calculate" > 
   <el-button type="primary" @click="handleCalculate">Calculate</el-button>
   </div>

   <div class="result" > 
      <span class="address"> 地址: </span>
      <el-input type="text" v-model="calresult" style="width: 240px" @change="handleCalculate" :readonly="true" />
   </div>

</template>
 
 <script lang="ts" setup>
import { calendarEmits } from 'element-plus';
import { ref } from 'vue'
 
 const blk= ref(1)
 const wl= ref(1)
 const string= ref(1)
 const calresult = ref(0)
 const handleChange = (value: blk) => {
   console.log(value)
 }
 const handleCalculate = () => {
   const result = (blk.value << (16+4) + wl.value * 6  + 4*string.value);
   calresult.value = result
 }

 </script>

 <style scoped>
   .input,.result {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
   }
   .wl,.string,.blk {
      padding: 20px;
   }
   .calculate {
     display: flex;
     justify-content: center;
     align-items: center;
     padding: 20px;
   }
 </style>
