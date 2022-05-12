import http from '@/services/http';

class VoxyService {
  countWords(payload: object): Promise<any> {
    return http.post('/api/wordcounting/wordCount', payload).then((response) => {
      return response;
    });
  }

  countWordsFile(file: any) {
    const formData = new FormData();
    formData.append('file', file);
    return http.post('/api/wordcounting/wordCountFile', formData, {
      headers: {
        'Content-Type': 'multipart/forma-data',
      },
    }).then((response) => {
      return response.data;
    });
  }
}

export default new VoxyService();
