import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { ThankYouPage } from '../thank-you/thank-you';

@Component({
  selector: 'page-product-invoice',
  templateUrl: 'product-invoice.html'
})
export class ProductInvoicePage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  constructor(public navCtrl: NavController) {
  }
  goToThankYou(params){
    if (!params) params = {};
    this.navCtrl.push(ThankYouPage);
  }
}
