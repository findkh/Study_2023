package com.kh.blockmanager.contoller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.kh.blockmanager.service.itemBoardService;

import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
public class itemBoardController {
	
	@Autowired
	itemBoardService itemBoardService;
	
	@RequestMapping(value = "/getItemList")
	public List<Map<String,Object>> getItemList() {
//		String returnValue = "hello";
//		return returnValue;
		return itemBoardService.getItemList();
	}

}
