const path = require('path')
const argv = require('minimist')(process.argv.slice(2));

let config = {}
let command = argv['_'][0]

switch(command) {
  case 'build':
    config = {
      baseUrl: '/static/gen',
      assetsDir: './',
      outputDir: '../idb/static/gen',
      indexPath: '../../templates/gen/index.html'
    }
    break
}

module.exports = config