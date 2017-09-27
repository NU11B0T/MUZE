import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { ProductScanPage } from '../product-scan/product-scan';
import { ProductInvoicePage } from '../product-invoice/product-invoice';
import { ProfilePage } from '../profile/profile';

@Component({
  selector: 'page-tabs-controller',
  templateUrl: 'tabs-controller.html'
})
export class TabsControllerPage {
  // this tells the tabs component which Pages
  // should be each tab's root Page
  tab1Root: any = ProductScanPage;
  tab2Root: any = ProductInvoicePage;
  tab3Root: any = ProfilePage;
  constructor(public navCtrl: NavController) {
  }
  
}
