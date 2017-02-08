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
                 $routeProvider.when('/people', {
                     templateUrl: 'static/partials/people.html',
                     controller: 'PeopleCtrl'});


                 $routeProvider.when('/ibm', {
                     templateUrl: 'static/partials/ibm.html',
                     controller: 'IbmCtrl'});



                 $routeProvider.when('/404', {
                     templateUrl: 'static/partials/404.html',
                     controller: 'FourOhFourCtrl'});
                 $routeProvider.otherwise({redirectTo: '/404'});
                 $locationProvider.html5Mode(true);
             }]);
