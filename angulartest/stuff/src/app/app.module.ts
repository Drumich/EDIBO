import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatSliderModule } from '@angular/material/slider';
import { WeatherModule } from './weather/weather.module';
import { CurrencyModule } from './currency/currency.module';


@NgModule({
  declarations: [
    AppComponent,
    // WeatherModule
  ],
  imports: [
    MatSliderModule,
    BrowserModule,
    BrowserAnimationsModule,
    CurrencyModule,
    // WeatherModule    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
