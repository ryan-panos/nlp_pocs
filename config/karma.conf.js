module.exports = function (config) {
  config.set({
    basePath: '../flaskular',

    files: [
      JASMINE,
      JASMINE_ADAPTER,
      'static/lib/angular/angular.js',
      'static/lib/angular/angular-*.js',
      'test/lib/angular/angular-mocks.js',
      'static/js/**/*.js',
      'test/unit/**/*.js'
    ],

    autoWatch: true,

    browsers: ['Chrome'],

    junitReporter: {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }
  });
}
