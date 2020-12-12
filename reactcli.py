import argparse
import textwrap
import subprocess
import os

class ReactCLI:
  def __init__(self):
    cli_parser = argparse.ArgumentParser("React CLI", "python reactcli [dir] --[options]", "A CLI to generate React boiler plate")
    cli_parser.add_argument('dir', type=str, metavar='dir', help='The directory where your files will be created')
    cli_parser.add_argument('--port',  default=4000, action='store', help='The port where the webserver will run from')
    cli_parser.add_argument('--ts', '-t',  action='store_true', help='Add support for typescript')
    cli_parser.add_argument('--sass', '-s', action='store_true', help='Add support for sass')
    cli_parser.add_argument('--eslint', '-l', action='store_true', help='Add Eslint support')
    args = cli_parser.parse_args()
    self.dir = args.dir
    print(self.dir)
    self.ts = args.ts
    self.sass = args.sass
    self.eslint = args.eslint
    self.port = args.port
    self.main()

  def main(self):
    self.__createDirectories()
    self.__initNpm()
    self.__create_webpack_server()
    self.__createTsConfigs()
    self.__createEslintrc()

  def __createDirectories(self):
    if self.dir != '.':
      os.mkdir(self.dir)
      os.chdir(self.dir)
      os.mkdir('src')

  def __initNpm(self):
    init_npm = ["npm", "init", "-y"]
    subprocess.run(init_npm)
    deps = ["npm", "install", "--save", "react", "react-dom"]
    subprocess.run(deps)
    dev_deps = ["npm", "install", "-D"]
    typescript_deps = ['@types/react', '@types/react-dom', 'ts-loader', 'typescript',]
    eslint_deps = ['eslint', 'eslint-config-airbnb', 'eslint-loader', 'eslint-plugin-import', 'eslint-plugin-jsx-a11y', 'eslint-plugin-react']
    sass_dps = ['node-sass', 'sass-loader']
    main_dev_deps = ['@babel/core', '@babel/preset-env', '@babel/preset-react', 'babel-loader', 'css-loader',  'file-loader', 'html-webpack-plugin', 'html-webpack-template', 'url-loader', 'webpack', 'webpack-cli', 'webpack-dev-server']
    dev_deps = dev_deps + main_dev_deps
    if self.ts:
      dev_deps = dev_deps + typescript_deps
    if self.sass:
      dev_deps = dev_deps + sass_dps
    if self.eslint:
      dev_deps = dev_deps + eslint_deps
    subprocess.run(dev_deps)

  def __createEslintrc(self):
    if self.eslint:
      with open(".eslintrc.json", "w") as f:
        f.writelines(textwrap.dedent('''\
          {
            "env": {
                "browser": true,
                "node": true,
                "es6": true
            },
            "extends": "airbnb",
            "globals": {
                "Atomics": "readonly",
                "SharedArrayBuffer": "readonly"
            },
            "parserOptions": {
                "ecmaFeatures": {
                    "jsx": true
                },
                "ecmaVersion": 2018,
                "sourceType": "module"
            },
            "plugins": [
                "react"
            ],
          }
        '''))

  def __createTsConfigs(self):
    if self.ts:
      with open('.tsconfig.json', 'w') as f:
        f.writelines(textwrap.dedent('''\
          {
            "compilerOptions": {
              "outDir": "./dist/",
              "allowUnreachableCode": false,
              "allowUnusedLabels": false,
              "declaration": true,
              "forceConsistentCasingInFileNames": true,
              "lib": ["es2016", "dom"],
              "module": "commonjs",
              "noEmitOnError": true,
              "noFallthroughCasesInSwitch": true,
              "noImplicitReturns": true,
              "pretty": true,
              "sourceMap": true,
              "strict": true,
              "target": "ESNext",
              "jsx": "react",
              "declarationDir": "./src/types/",
              "experimentalDecorators": true
            },
            "include": [
              "./src"
            ],
            "exclude": [
              "node_modules"
            ]
          }
        '''))
      with open('.tslint.json', 'w') as f:
        f.writelines(textwrap.dedent('''\
          {
            "rules": {
              "array-type": [true, "array-simple"],
              "arrow-return-shorthand": true,
              "ban": [true,
                {"name": ["it", "skip"]},
                {"name": ["it", "only"]},
                {"name": ["it", "async", "skip"]},
                {"name": ["it", "async", "only"]},
                {"name": ["describe", "skip"]},
                {"name": ["describe", "only"]},
                {"name": "parseInt", "message": "tsstyle#type-coercion"},
                {"name": "parseFloat", "message": "tsstyle#type-coercion"},
                {"name": "Array", "message": "tsstyle#array-constructor"},
                {"name": ["*", "innerText"], "message": "Use .textContent instead. tsstyle#browser-oddities"}
              ],
              "ban-ts-ignore": true,
              "ban-types": [true,
                ["Object", "Use {} instead."],
                ["String", "Use 'string' instead."],
                ["Number", "Use 'number' instead."],
                ["Boolean", "Use 'boolean' instead."]
              ],
              "class-name": true,
              "curly": [true, "ignore-same-line"],
              "deprecation": true,
              "forin": true,
              "interface-name": [true, "never-prefix"],
              "interface-over-type-literal": true,
              "jsdoc-format": true,
              "label-position": true,
              "member-access": [true, "no-public"],
              "new-parens": true,
              "no-angle-bracket-type-assertion": true,
              "no-any": true,
              "no-arg": true,
              "no-conditional-assignment": true,
              "no-construct": true,
              "no-debugger": true,
              "no-default-export": true,
              "no-duplicate-variable": true,
              "no-inferrable-types": true,
              "no-namespace": [true, "allow-declarations"],
              "no-reference": true,
              "no-string-throw": true,
              "no-return-await": true,
              "no-unsafe-finally": true,
              "no-unused-expression": true,
              "no-var-keyword": true,
              "object-literal-shorthand": true,
              "only-arrow-functions": [true, "allow-declarations", "allow-named-functions"],
              "prefer-const": true,
              "radix": true,
              "semicolon": [true, "always", "ignore-bound-class-methods"],
              "switch-default": true,
              "exp"
              "trailing-comma": [
                true,
                {
                  "multiline": {
                    "objects": "always",
                    "arrays": "always",
                    "functions": "never",
                    "typeLiterals": "ignore"
                  },
                  "esSpecCompliant": true
                }
              ],
              "triple-equals": [true, "allow-null-check"],
              "use-isnan": true,
              "variable-name": [
                true,
                "check-format",
                "ban-keywords",
                "allow-leading-underscore",
                "allow-trailing-underscore"
              ]
            }
          }
        '''))

  def __createBabelrc(self):
    with open('.babelrc', 'w') as f:
      f.writelines(textwrap.dedent('''\
        {
          "presets": [
              "@babel/preset-react",
              ["@babel/preset-env",
              {
                "modules": false
              }],
            ],
        }
        '''))

  def __entryOutput(self):
      entry = textwrap.indent('''\
      entry: './src/index.%s',
      output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].[contenthash].js'
      },\
      ''' % ('tsx' if self.ts else 'jsx'), ' ' * 2)
      return entry

  def __devServer(self):
      server = textwrap.indent('''\
      devServer: {
        index: 'index.html',
        port: %s,
        contentBase: path.join(__dirname, 'dist'),
      },\
      ''' % (self.port), ' ' * 2)
      return server

  def __rules(self):
      tsx_rules = textwrap.indent('''\
      {
        test: /\.(ts|tsx)?$/,
        loader: 'ts-loader',
        exclude: /node_modules/
      },\
      ''', ' ' * 4)
      sass_rules = textwrap.indent('''\
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader'
        ]
      },\
      ''',' ' * 4)
      image_rules = textwrap.indent('''\
      {
        test: /\.svg$/,
        use: 'file-loader'
      },
      {
        test: /\.png$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              mimetype: 'image/png'
            }
          }
        ]
      }
      ''', ' '*4)
      if self.sass and self.ts:
        image_rules = sass_rules + tsx_rules + image_rules
      elif self.sass and not self.ts:
        image_rules = sass_rules + image_rules
      elif self.ts and not self.sass:
        image_rules = tsx_rules + image_rules
      base = textwrap.indent('''\
      module: {
        rules: [
          {
            test: /\.(js|jsx)$/,
            use: 'babel-loader',
            exclude: /node_modules/
          },
          {
            test: /\.css$/,
            use: [
              'style-loader',
              'css-loader'
            ]
          },
          %s
        ]
      },\
      ''' % image_rules, ' ' * 2)
      return base

  def __create_webpack_server(self):
    with open('webpackDevServer.js', 'wt', encoding='UTF-8') as f:
      entry_output = str(self.__entryOutput())
      dev_server = str(self.__devServer())
      additional_rules = str(self.__rules())


      f.writelines(textwrap.dedent('''\
      const webpack = require('webpack');
      const path = require('path');
      const HtmlWebpackPlugin = require('html-webpack-plugin');

      const config = {
  %s
  %s
  %s
        resolve: {
          extension: [
            '.js',
            '.jsx',
            '.tsx',
            '.ts'
          ]
        },
        plugins: [
          new HtmlWebpackPlugin({
            template: require('html-webpack-template'),
            inject: false,
            appMountId: 'app',
          })
        ],
        optimization: {
          runtimeChunk: 'single',
          splitChunks: {
            cacheGroups: {
              vendor: {
                test: /[\\\/]node_modules[\\\/]/,
                name: 'vendors',
                chunks: 'all'
              }
            }
          }
        }
      };
      module.exports = config;
        ''' % (entry_output, dev_server, additional_rules)))

if __name__ == "__main__":
    ReactCLI()