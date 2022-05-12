<template>
  <div class="w-4/5 flex flex-col items-center">
    <h1 class="text-3xl">ByCoders TESTE Leia REAMDE.md</h1>

    <h2 class="text-2xl">
      <a href="/api/apidocs/" target="_blank">Documentação dos ENDPOINTS</a>
    </h2>

    <div class="w-1/2 flex flex-col items-center m-2">
      <h3> Adicione seu arquivo aqui</h3>

      <div class="w-full h-12 flex justify-center items-center bg-light-gray rounded-lg border border-solid m-2 cursor-pointer" @click="$refs.file.click()">
        <span v-if="!uploadFile"> click here to upload</span>
        <div v-else>
          <span @click="uploadFile=null" class="x-button"> X </span>
          <span> File name: {{ uploadFile.name }} </span>
        </div>

        <input type="file" id="upload" ref="file" @input="changeInputFile" accept="text/plain" style="display: none">
      </div>

      <div class="w-full h-24 flex justify-center items-center bg-light-gray rounded-lg border border-solid m-2">
        <textarea v-model="sentence">

        </textarea>
      </div>

      <div class="w-full flex justify-end space-x-2">
        <button class="w-36 rounded-lg border border-green border-solid p-2 border-red-500 hover:bg-red-300 hover:text-white"
          @click="submitToCount" :disabled="!uploadFile"> Cancel </button>

        <button class="w-36 rounded-lg border border-green border-solid p-2 text-white bg-green-400 hover:bg-green-600"
          @click="submitToCount"> Submit </button>
      </div>
    </div>

    <div class="w-full flex flex-col">
      <h2> Word Analytical </h2>

      <div v-if="countResponse.count > 0">
        <div class="w-full"> Total words: {{ countResponse.count }}</div>

        <div class="w-full grid grid-cols-6 gap-4">
          <div v-for="item in countResponse.characters" :key="item.character" class="rounded-lg border-solid border p-2"
               :class="{'bg-green-400': item.count > 0}">
            <span> {{ item.character }}: {{ item.count }} </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import VoxyService from '@/services/voxyService';
import { WordCountResponse } from '@/types/Char';

@Component
export default class WordCounter extends Vue {
  private uploadFile: null | File = null;

  private sentence: string;

  private countResponse: WordCountResponse;

  constructor() {
    super();
    this.sentence = '';
    this.countResponse = {
      count: 0,
      characters: [],
    };
  }

  changeInputFile(e: any) {
    const file = e.target.files || e.dataTransfer.files;

    // eslint-disable-next-line prefer-destructuring
    this.uploadFile = file[0];
    e.currentTarget.value = '';
  }

  submitToCount(): Promise<boolean> {
    if (this.uploadFile) {
      return VoxyService.countWordsFile(this.uploadFile).then((response: WordCountResponse) => {
        this.uploadFile = null;
        this.countResponse = response;
        return true;
      });
      // eslint-disable-next-line no-else-return
    } else {
      const payload = {
        sentence: this.sentence,
      };
      return VoxyService.countWords(payload).then((response) => {
        this.countResponse = response.data;
        return true;
      }).catch((err) => {
        console.error(err);
        return false;
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }

  //.content-box {
  //  width: 64rem;
  //  display: flex;
  //  flex-direction: column;
  //  justify-content: center;
  //  align-items: center;
  //
  //  &.content-area {
  //    width: 90% !important;
  //    display: flex;
  //    flex-direction: column;
  //    justify-content: center;
  //    align-items: center;
  //  }
  //}

  .upload_box {
    width: 100%;
    height: 3rem;
    display: flex;
    justify-content: space-around;
    align-items: center;
    text-align: center;

    border-width: 1px;
    border-style: solid;
    border-color: darkgrey;
    cursor: pointer;

    .x-button {
    border-width: 1px;
    border-style: solid;
    border-color: red;

    &:hover {
      background-color: red;
      border-color: darkgrey;
    }
  }
  }

  .store-grid {
    width: 32rem;
  }

  .transaction-grid {
    width: 48rem;
  }

  .store-header {
    width: 100%;
    height: 28px;
    display: flex;
    justify-content: space-around;
    align-items: center;

    border-width: 0;
    border-bottom-width: 1px;
    border-style: solid;
    border-color: darkgrey;
  }

  .store-body-row {
    width: 100%;
    height: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    //background-color: lightgrey;
    &:nth-child(even) {
      background-color: lightgrey;
    }

    .justify-start {
      display: flex;
      justify-content: flex-start;
    }

    .justify-center {
      display: flex;
      justify-content: center;
    }
  }

  .bg-red {
    background-color: rgba(255, 0, 0, 0.5) !important;
  }
  .bg-green {
    background-color: rgba(144, 238, 144, 0.48) !important;
  }

  .transaction-store-header {
    height: 32px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-width: 2px 0px;
    border-style: solid
  }
</style>
