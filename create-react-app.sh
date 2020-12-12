#!/bin/bash
echo "Creating package.json..."
npm init -y
echo "Creating webpack config..."
python createWebpack.py
echo "Installing dependencies..."
npm install --save react react-dom
echo "Installing dev dependencies..."
npm install -D \
    @babel/core @babel/preset-env @babel/preset-react \
    @types/react @types/react-dom babel-loader css-loader\
    eslint eslint-config-airbnb eslint-loader eslint-plugin-import \
    eslint-plugin-jsx-a11y eslint-plugin-react file-loader \
    html-webpack-plugin html-webpack-template node-sass \
    sass-loader ts-loader typescript url-loader webpack \
    webpack-cli webpack-dev-server