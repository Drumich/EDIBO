import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

import { map } from 'rxjs/operators';

// interface RateDateRates {
//   [k: string]: { [k: string]: number }
// }                      // ^ this is for currency stuff

// interface RateData { // currency stuff
interface WeatherData {
  date: string;
  temperatureC: number;
  temperatureF: number;
  summary: string;
  // start_at: string;  // currency stuff
  // base: string;  // currency stuff
  // end_at: string;  // currency stuff
  // rates: RateDateRates; // currency stuff
}

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.scss'],
})
export class WeatherComponent implements OnInit {

  // baseRate = 'EUR';
  // symbols = 'USD,GBP';
  weatherData: any;
  Temperature: [string, any][];

  // startDate: string;
  // endDate: string;
  // rates: any[];





  constructor(private restClient: HttpClient) {}

  ngOnInit(): void {
    this.restClient
      .get<WeatherData>(this.getTemperaturesUrl())
      .subscribe((data) => this.processData(data));
  }

  processData(data: WeatherData): void {
    this.Temperature = Object.entries(data);
      map(divainiba=>({
        date: divainiba[0],
        temperatureC: divainiba[1],
        temperatureF: divainiba[2],
        summary: divainiba[3]
      }));
    }
  

  // processData(data: WeatherData): void {
  //   this.startDate = data.start_at;
  //   this.endDate = data.end_at;
  //   this.rates = Object.entries(data.rates)
  //   .map(divainiba=>({
  //     date: divainiba[0],
  //     rate: divainiba[1]
  //   }));
  // }

  getTemperaturesUrl(): string {
    return environment.temperaturesUrl;
      // .replace('{base}', this.baseRate)
      // .replace('{symbols}', this.symbols);
  }
}
