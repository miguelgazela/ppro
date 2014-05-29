module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            dist: {
                src: [
                    'proteil/static/proteil/js/*.js' // All JS files in the JS folder
                ],
                dest: 'proteil/static/proteil/js/dist/production.js',
            }
        },

        uglify: {
            build: {
                src: 'proteil/static/proteil/js/dist/production.js',
                dest: 'proteil/static/proteil/js/dist/production.min.js'
            }
        },

        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'proteil/static/proteil/images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'proteil/static/proteil/images/'
                }]
            }
        },

        watch: {
            options: {
                livereload: true,
            },

            scripts: {
                files: ['proteil/static/proteil/js/*.js'],
                tasks: ['concat', 'uglify'],
                options: {
                    spawn: false,
                },
            },

            css: {
                files: ['proteil/static/proteil/css/*.scss'],
                tasks: ['sass'],
                options: {
                    spawn: false,
                },
            },
        },

        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'proteil/static/proteil/css/global.css': 'proteil/static/proteil/css/global.scss'
                }
            }
        }
    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat', 'uglify', 'imagemin', 'sass', 'watch']);

};