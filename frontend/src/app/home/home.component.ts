import { Component, OnInit } from '@angular/core';
import { UploadService } from '../services/upload.service';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  loading = false;
  load = true;
  selectedColunms: any[] = [];
  allColunms = ['PName', 'Customer Age']
  constructor(private uploadService: UploadService) { }
  ngOnInit(): void {
  }
  allData: any[] = []

  iterationCount: number[] = Array.from({ length: 5 }, (_, index) => index);
  columnNumber: number = 7
  imageUrl: any[] = [];

  scroll(el: HTMLElement) {
    el.scrollIntoView({ behavior: 'smooth' });
  }

  message: string | null = null;
  selectedFile: any;
  onFileChange(event: any) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.selectedFile = (btoa(e.target.result));
        // this.create(file,index)
      };
      reader.readAsBinaryString(file);
    }
  }
  hideloader() {
    let d = document.getElementById('loading');
    if (d)
      d.style.display = 'none';
  }

  uploadFile() {
    if (!this.selectedFile) {
      this.message = 'Please select a file.';
      return;
    }
    this.load = false;
    this.loading = true;
    this.allData = []
    this.imageUrl = [];
    console.log(this.selectedFile)
    this.uploadService.uploadFile(this.selectedFile)
      .subscribe(
        (data) => {

          this.allData = data

         
        }
      );
  }

}
