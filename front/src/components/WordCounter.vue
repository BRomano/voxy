<template>
  <div class="w-4/5 flex flex-col items-center">
    <h1 class="text-3xl underline m-2">
      <a href="https://github.com/BRomano/voxy" target="_blank">Voxy TESTE Leia REAMDE.md</a>
    </h1>

    <h2 class="text-2xl underline">
      <a href="/api/apidocs/" target="_blank">Documentação dos ENDPOINTS</a>
    </h2>

    <div class="w-1/2 flex flex-col items-center m-2">
      <div class="w-full h-12 flex justify-center items-center bg-light-gray rounded-lg border border-solid m-2 cursor-pointer" @click="$refs.txtFile.click()">
        <span v-if="!uploadFile"> click here to upload a file</span>
        <div v-else>
          <span> File name: {{ uploadFile.name }} </span>
        </div>

        <input type="file" id="upload" ref="txtFile" @input="changeInputFile" accept="text/plain" style="display: none">
      </div>

      <div class="w-full flex flex-col">
        <div class="w-full h-24 flex flex-col justify-center items-center bg-light-gray rounded-lg border border-solid m-2" :class="{'border-red-300': error}">
          <textarea v-model="sentence" class="w-full h-24 focus:border-green-300"></textarea>
        </div>

        <div v-if="error" class="w-full flex justify-start">
          <span class="text-red-600">* {{ error }} </span>
        </div>
      </div>

      <div class="w-full flex justify-end space-x-2">
        <button class="w-36 rounded-lg border border-green border-solid p-2 border-red-500 hover:bg-red-300 hover:text-white"
          @click="clean"> Clean </button>

        <button class="w-36 rounded-lg border border-green border-solid p-2 text-white bg-green-400 hover:bg-green-600"
          @click="submitToCount"> Submit </button>
      </div>
    </div>

    <div class="w-full flex flex-col">
      <div v-if="countResponse.count > 0">
        <h2 class="text-2xl"> Word Analytical </h2>
        <div class="w-full"> Total words: {{ countResponse.count }}</div>

        <h2 class="text-2xl mt-2"> Total Characters </h2>
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
  private uploadFile: File | null;

  private sentence: string;

  private error: string;

  private countResponse: WordCountResponse;

  constructor() {
    super();

    this.uploadFile = null;
    this.sentence = '';
    this.error = '';
    this.countResponse = new WordCountResponse();
  }

  changeInputFile(e: any) {
    const files = e.target.files || e.dataTransfer.files;

    // eslint-disable-next-line prefer-destructuring
    this.uploadFile = files[0];
    if (this.uploadFile) {
      this.uploadFile.text().then((txt: string) => {
        this.sentence = txt.substring(0, 200).concat('...');
      });
    }
    e.currentTarget.value = '';
  }

  submitToCount(): Promise<boolean> {
    let promise = null;
    if (this.uploadFile) {
      promise = VoxyService.countWordsFile(this.uploadFile).then((response: WordCountResponse) => {
        this.uploadFile = null;
        this.countResponse = response;
        return true;
      });
      // eslint-disable-next-line no-else-return
    } else {
      const payload = {
        sentence: this.sentence,
      };
      promise = VoxyService.countWords(payload).then((response) => {
        this.countResponse = response.data;
        return true;
      });
    }

    promise.then(() => {
      this.error = '';
    }).catch((err) => {
      this.error = err.response.data.message;
      return false;
    });

    return promise;
  }

  clean(): void {
    this.uploadFile = null;
    this.countResponse = new WordCountResponse();
    this.sentence = '';
    this.error = '';
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
