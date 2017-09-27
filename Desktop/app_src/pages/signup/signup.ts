import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { LoginPage } from '../login/login';
import { SignupPage } from '../signup/signup';
import { ProductScanPage } from '../product-scan/product-scan';
import { BarcodeScannerPage } from '../barcode-scanner/barcode-scanner';
import { ProductScanPage } from '../product-scan/product-scan';

@Component({
  selector: 'page-signup',
  templateUrl: 'signup.html'
})
export class SignupPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  constructor(public navCtrl: NavController) {
  }
  goToLogin(params){
    if (!params) params = {};
    this.navCtrl.push(LoginPage);
  }goToSignup(params){
    if (!params) params = {};
    this.navCtrl.push(SignupPage);
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
