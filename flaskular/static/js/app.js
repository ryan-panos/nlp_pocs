'use strict';


// Declare app level module which depends on filters, and services
angular.module('Flaskular', ['Flaskular.filters',
                             'Flaskular.services',
                             'Flaskular.directives',
                             'Flaskular.controllers'])
    .config(['$routeProvider', '$locationProvider',
             function($routeProvider, $locationProvider) {
                 $routeProvider.when('/', {
                     templateUrl: 'static/partials/home.html',
                     controller: 'HomeCtrl'});
                 $routeProvider.when('/about', {
                     templateUrl: 'static/partials/about.html'});
                 $routeProvider.when('/contact', {
                     templateUrl: 'static/partials/contact.html',
                     controller: 'ContactCtrl'});
                 $routeProvider.otherwise({redirectTo: '/404'});
                 $locationProvider.html5Mode(true);
             }]);
