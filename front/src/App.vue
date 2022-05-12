<template>
  <div id="app">
    <WordCounter />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import WordCounter from '@/components/WordCounter.vue';

@Component({
  components: {
    WordCounter,
  },
})
export default class App extends Vue {}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  justify-content: center;
}
</style>
