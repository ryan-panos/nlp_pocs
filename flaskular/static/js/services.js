'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('Flaskular.services', []).
  value('version', '0.1');


angular.module('Flaskular.services', ['ngResource'])
    .factory('Person', function($resource) {
        return $resource('/api/people/:personId', {}, {
            query: {
                method: 'GET',
                params: { personId: '' },
                isArray: false
            }
        });
    });


angular.module('Flaskular.services', ['ngResource'])
    .factory('TestIBMService', function($resource) {
        return $resource('/api/testIBM/', {}, {
            queryAll: {
                method: 'GET',
                params: {  },  // personId: ''
                isArray: true
            },
            queryMany: {
                method: 'GET',
                params: { is_many: "True" },  // personId: ''
                isArray: true
            },
            queryTarget: {
                method: 'GET',
                params: { is_target: "True" },  // personId: ''
                isArray: true
            }
        });
    });

console.log(">   LOADING!!! TestIBMService!! ");