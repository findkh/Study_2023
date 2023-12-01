package com.springboot.security;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {

	@GetMapping("/hello")
	public String hello() {
		return "Test Hello";
	}
	
	@GetMapping("/hi")
	public String hi() {
		return "hi";
	}
	
}
