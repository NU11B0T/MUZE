import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { ProductScanPage } from '../product-scan/product-scan';
import { BarcodeScannerPage } from '../barcode-scanner/barcode-scanner';

@Component({
  selector: 'page-barcode-scanner',
  templateUrl: 'barcode-scanner.html'
})
export class BarcodeScannerPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  constructor(public navCtrl: NavController) {
  }
  goToProductScan(params){
    if (!params) params = {};
    this.navCtrl.push(ProductScanPage);
  }goToBarcodeScanner(params){
    if (!params) params = {};
    this.navCtrl.push(BarcodeScannerPage);
  }
}
