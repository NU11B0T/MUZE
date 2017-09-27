import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';
import { ProductScanPage } from '../pages/product-scan/product-scan';
import { ProductInvoicePage } from '../pages/product-invoice/product-invoice';
import { ThankYouPage } from '../pages/thank-you/thank-you';
import { TabsControllerPage } from '../pages/tabs-controller/tabs-controller';
import { WelcomeToHULPage } from '../pages/welcome-to-hul/welcome-to-hul';
import { BarcodeScannerPage } from '../pages/barcode-scanner/barcode-scanner';
import { SignupPage } from '../pages/signup/signup';
import { LoginPage } from '../pages/login/login';
import { ProfilePage } from '../pages/profile/profile';


import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

@NgModule({
  declarations: [
    MyApp,
    ProductScanPage,
    ProductInvoicePage,
    ThankYouPage,
    TabsControllerPage,
    WelcomeToHULPage,
    BarcodeScannerPage,
    SignupPage,
    LoginPage,
    ProfilePage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    ProductScanPage,
    ProductInvoicePage,
    ThankYouPage,
    TabsControllerPage,
    WelcomeToHULPage,
    BarcodeScannerPage,
    SignupPage,
    LoginPage,
    ProfilePage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}