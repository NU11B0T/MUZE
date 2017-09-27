import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { BarcodeScannerPage } from '../barcode-scanner/barcode-scanner';
import { ProductScanPage } from '../product-scan/product-scan';

@Component({
  selector: 'page-product-scan',
  templateUrl: 'product-scan.html'
})
export class ProductScanPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  constructor(public navCtrl: NavController) {
  }
  goToBarcodeScanner(params){
    if (!params) params = {};
    this.navCtrl.push(BarcodeScannerPage);
  }goToProductScan(params){
    if (!params) params = {};
    this.navCtrl.push(ProductScanPage);
  }
}
