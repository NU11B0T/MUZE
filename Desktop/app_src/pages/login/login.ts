import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { SignupPage } from '../signup/signup';
import { LoginPage } from '../login/login';
import { ProductScanPage } from '../product-scan/product-scan';
import { BarcodeScannerPage } from '../barcode-scanner/barcode-scanner';
import { ProductScanPage } from '../product-scan/product-scan';

@Component({
  selector: 'page-login',
  templateUrl: 'login.html'
})
export class LoginPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  constructor(public navCtrl: NavController) {
  }
  goToSignup(params){
    if (!params) params = {};
    this.navCtrl.push(SignupPage);
  }goToLogin(params){
    if (!params) params = {};
    this.navCtrl.push(LoginPage);
  }goToProductScan(params){
    if (!params) params = {};
    this.navCtrl.push(ProductScanPage);
  }goToBarcodeScanner(params){
    if (!params) params = {};
    this.navCtrl.push(BarcodeScannerPage);
  }goToProductScan(params){
    if (!params) params = {};
    this.navCtrl.push(ProductScanPage);
  }
}
