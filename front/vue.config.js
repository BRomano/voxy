const path = require('path');

module.exports = {
  // outputDir: './front/dist',
  // assetsDir: './front/web',
  pages: {
    index: {
      entry: './src/main.ts',
      template: 'public/index.html',
      filename: 'index.html',
    },
  },
  chainWebpack: (config) => {
    config.resolve.alias
      .set('@', path.join(__dirname, './src'));
  },
};
