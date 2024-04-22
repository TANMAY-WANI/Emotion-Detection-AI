// file-upload.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UploadService {

  constructor(private http: HttpClient) { }

  uploadFile(file: any) {

    return this.http.post<any>('http://localhost:3000/upload', file);
  }

}
