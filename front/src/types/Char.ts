export interface Char {
  character: string;
  count: number;
};

export class WordCountResponse {
  count: number;

  characters: Array<Char>;

  constructor() {
    this.count = 0;
    this.characters = [];
  }
}
