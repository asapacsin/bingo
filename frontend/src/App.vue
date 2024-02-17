<script>
import axios from "axios";
export default{
  data(){
    return {
      msg :' hello world',
      current_number:0,
      tmp_dict:[],
      record:[]
    };
  },
  methods:{
    getMessage(){
      axios.get("/").then((res)=>{
        console.log(res)
        if (res.data == -1){
          alert("已經抽完號碼")
        }
        else{
          [this.current_number,this.tmp_dict] = res.data;
          this.record = this.tmp_dict['record']
        }
      });
    },
    reflesh(){
      axios.get("/reflesh/").then((res)=>{
        this.tmp_dict = res.data;
        this.current_number = 0;
        this.record = this.tmp_dict['record']
      })
    },
    getAll(){
      axios.get("/getAll/").then((res)=>{
        [this.current_number,this.tmp_dict] = res.data;
        this.record = this.tmp_dict['record']
      })
    }
  },
};
</script>

<template>
  <div class="button-area">
    <button @click="getMessage" class="button">抽號</button>
    <button @click="reflesh" class="button">重置</button>
    <button @click="getAll" class="button" hidden>取得全部</button>
    <div class="number-area">
      <p>目前號碼: {{current_number}}</p>
    </div>
  </div>
  
  <div class="record-area">
    <p>歷史號碼: {{record}}</p>
  </div>
  
  
</template>

<style scoped>
.record-area{
  width:480px;
}
.button-area{
  position:absolute;
  left:240px;
  top:140px;
  width:240px;
  height:140px;
}
.number-area{
  padding:10px;
}
.record-area{
  position: absolute;
  top:350px;
  left:240px;
}
.button{
  height:50px;
  width:100px;
  margin:10px;
}
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
