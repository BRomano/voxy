export interface Char {
  character: string;
  count: number;
};

export interface WordCountResponse {
  count: number;
  characters: Array<Char>;
}
