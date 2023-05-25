package com.kh.blockmanager.test_controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RestController
@RequiredArgsConstructor
@Slf4j
public class ServiceContoller {

    @RequestMapping("/greetingNoParamTest")
	public String greetingNoParamTest() {

		log.info("greeting..");
		String returnValue = "OK";

		return returnValue;
	}
	    
}
