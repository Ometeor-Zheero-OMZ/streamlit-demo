code = """
// 参照カウント付きのポインタ　ノードの所有権の共有を可能にさせる
use std::rc::Rc;
// 内部可変性を可能にする
use std::cell::RefCell;

#[derive(Debug)]
struct Node<T> {
    data: T,
    prev: Option<Rc<RefCell<Node<T>>>>,
    next: Option<Rc<RefCel<Node<T>>>>,
}

pub struct DoublyLinkedList<T> {
    head: Option<Rc<RefCell<Node<T>>>>,
    tail: Option<Rc<RefCell<Node<T>>>>,
}

/*
 * Rc<RefCell<T>>で内部可変性の特性を持つポインタを定義できる
 */

impl<T> DoublyLinkedList<T> {
    /// 空のリストを作成
    pub fn new() -> Self {
        DoublyLinkedList { head: None, tail: None }
    }

    /// リストの末尾に要素を追加
    pub fn push_back(&mut self, data: T) {
        let new_node = Rc::new(RefCell::new(Node {
            data,
            prev: self.tail.clone(),
            next: None,
        }));

        if let Some(tail) = &self.tail {
            tail.borrow_mut().next = Some(new_node.clone());
        }

        self.tail = Some(new_node);

        if self.head.is_none() {
            self.head = Some(new_node.clone());
        }
    }

    /// リストの先頭に要素を追加
    pub fn push_front(&mut self, data: T) {
        let new_node = Rc::new(RefCell::new(Node {
            data,
            prev: None,
            next: self.head.clone()
        }));

        if let Some(head) = &self.head {
            head.borrow_mut().prev = Some(new_node.clone())
        }

        self.head = Some(new_node);

        if self.tail.is_none() {
            self.tail = Some(new_node.clone());
        }
    }

    /// リストの先頭から要素を削除
    pub fn pop_front(&mut self) -> Option<T> {
        self.head.take().map(|head| {
            if let Some(next) = head.borrow_mut().next.take() {
                next.borrow_mut().prev == None;
                self.head = Some(next);
            } else {
                self.tail = None;
            }

            // ノードを解放し、所有権を取り戻す。
            Rc::try_unwrap(head)
                .ok()
                .expect("Failed to unwrap Rc")
                .into_inner()
                .data
        })
    }

    /// リストの末尾から要素を削除
    pub fn pop_back(&mut self) -> Option<T> {
        self.tail.take().map(|tail| {
            if let Some(prev) = tail.borrow_mut().prev.take() {
                prev.borrow_mut().next = None;
                self.tail = Some(prev);
            } else {
                self.head = None;
            }

            Rc::try_unwrap(tail)
                .ok()
                .expect("Failed to unwrap Rc")
                .into_inner()
                .data
        })
    }

    /// リストの全要素を表示
    pub fn display(&self) {
        let mut curr = self.head.clone();
        while let Some(node) = curr {
            print!("{:?}", node.borrow().data);
            curr = node.borrow().next.clone();
        }
        println!();
    } 
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn tests_double_linked_list() {
        let mut list = DoublyLinkedList::new();

        list.push_back(1);
        list.push_back(2);
        list.push_back(3);
        list.push_front(10);

        // 5 1 2 3
        list.display();

        list.pop_front();

        // 1 2 3
        list.display();

        list.pop_back();

        // 1 2
        list.display();
    }
}
"""